from functools import lru_cache
class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
 
        @lru_cache(None)
        def singlelen(n: int) :
            if not isinstance(n, int):
                print(n)
            if n <= 1:
                return n
            elif n < 10:
                return 2
            elif n < 100:
                return 3
            else:
                return 4
            
        def encode(s):
            last, len = '' , 0
            res = []
            for c in s:
                if c == last:
                    len += 1
                else :
                    if last != '':
                        res.append((last, len))
                    last, len = c, 1
            if len != 0:
                res.append((last, len))
            return res
        def add(curchar, curlen: int , code):
            #print(32, type(curlen), end= ' ')
            if len(code) == 0:
                return 0, curchar, curlen 
            
            prevsum  = 0
            for n, l in code:
                if n == curchar:
                    curlen += l
                else:
                    prevsum += singlelen(curlen)
                    curchar, curlen = n, l  
                    #print(43, type(curlen), end= ' ')
            return (prevsum, curchar, curlen) 
        
        @lru_cache(None)
        def dp(code, remain, todel, curchar, curlen: int):
            #print(sum(tuple(zip(*code))[1]), remain, todel, curchar, curlen)
            if remain == todel:
                #print(49, type(curlen), end= ' ')
                return singlelen(curlen)
            if todel == 0:
                (prelen, curchar, curlen) = add(curchar, curlen, code)
                #print(53, type(curlen), end= ' ')
                return prelen + singlelen(curlen)
            
            if len(code) < 1 or len(code[0]) < 1: 
                print((57, code, remain, todel, curchar, curlen))
            if code[0][0] == curchar:
                curlen += code[0][1]
                remain -= code[0][1]
                if remain < todel:
                    curlen += todel - remain
                    remain = todel
                    return singlelen(curlen)
                else:
                    code = code[1:]
                if len(code) == 0:
                    return singlelen(curlen)
                
            cases = []
            
            if todel >= code[0][1]:
                #print(63, type(curlen), end= ' ')
                cases.append(dp(code[1:], remain - code[0][1], todel - code[0][1], curchar, curlen))
        
            (prelen, newchar, newlen) = add(curchar, curlen, code[:1]) 
            #print(67, type(newlen), end= ' ') 
            for trydel in range(max(0, todel - remain + code[0][1] ),  min(code[0][1], todel + 1)) :
                cases.append(prelen  + dp(code[1:], remain - code[0][1], todel - trydel, newchar, newlen - trydel))

            # remove all current stride, remove partial of current stride, keep current stride 
        
            if len(cases) == 0:
                #81       4                          1       1      b        3       -  0       b        5
                #  (('b', 2), ('a', 1), ('c', 1)) ((0, 2), (2, 2))
                #81       2                          1       1      c        4       -  0       c        6 
                # | (('c', 2),)  ((0, 2), (2, 2))
                print((81, sum(tuple(zip(*code))[1]), remain, todel, curchar, curlen,'-',prelen, newchar, newlen, '|', code, ((0, todel - remain + code[0][1] ),  (code[0][1], todel + 1))))
            return min(cases)
        
    
        code = tuple( encode(s))
        print((code, len(s))) 
        print((sum(tuple(zip(*code))[1])))
        
        return dp( code, len(s), k, '', 0)
    
    def getLengthOfOptimalCompression2(self, s: str, k: int) -> int:
        N = len(s)
        if N == k:
            return 0
        @lru_cache(None)
        def singlelen(n) :
            if n <= 1:
                return n
            elif n < 10:
                return 2
            elif n < 100:
                return 3
            else:
                return 4
                
        def finallen(prev):
            return prev[0] + singlelen(prev[1]) 
        
        def add(prev, s):
            if len(s) == 0:
                return prev 
            
            prevsum, curlen, cur = prev
            for n in s:
                if n == cur:
                    curlen += 1
                else:
                    prevsum += singlelen(curlen)
                    curlen, cur= 1, n  
                
            return (prevsum, curlen, s[-1:]) 
        
        @lru_cache(None)
        def dp(s, k, prev):
            if k == 0:
                return finallen(add(prev, s))
            if len(s) == k:
                return finallen(prev)

            cur, s = s[:1], s[1:]
            while cur == prev[2] and len(s) > k:
                prev = add(prev,cur) 
                cur, s = s[:1], s[1:] 

            return min (dp(s, k - 1, prev), dp(s, k, add(prev,cur))) 
        
        return dp(s, k, (0, 0, ''))

