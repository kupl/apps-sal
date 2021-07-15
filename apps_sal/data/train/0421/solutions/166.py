class Solution:
    def lastSubstring(self, s: str) -> str:
        def helper(s, start = 0):
            p1, p2 = start, -1
            # for i, l in enumerate(s): 
            for i in range(start+1, len(s)): 
                l = s[i]
                if p2 > 0: 
                    # has valid start
                    if ord(l) > ord(s[p1 + i-p2]): 
                        p1 = p2

                    elif ord(l) == ord(s[p1 + i-p2]): 
                        pass
                    else: 
                        p2 = -1                
                else:
                    # how you initialize the string
                    if ord(l) > ord(s[p1]): 
                        p1 = i
                    elif ord(l) < ord(s[p1]): 
                        pass
                    else: 
                        p2 = i
            # return s[p1:]
            return p1
        
        i, j = 0, helper(s, 0)
        while j > i: 
            i, j = j, helper(s, j)
        return s[j:]
        
        # ans = helper(s, 0)
        # while len(s) > len(ans): 
        #     s, ans = ans, helper(ans)
        # return ans
        
        
        

