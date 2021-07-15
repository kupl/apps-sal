class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        if not len(s)==len(t): return False
        
        n = len(s)
        count = defaultdict(int)
        for i in range(n):
            if s[i]!=t[i]:
                temp = -ord(t[i])+ord(s[i])
                count[ (temp+26)%26 ] += 1
            
        k1,k2 = k//26,k%26
        helper = defaultdict(int)
        for i in range(1,26):
            helper[i] += k1

        if k2:
            for i in range(1,k2+1):
                helper[26-i] += 1
                    
        print(count)
        print(helper)
        
        for i in count:
            if not (i in helper) or helper[i]<count[i]:
                return False
        return True
