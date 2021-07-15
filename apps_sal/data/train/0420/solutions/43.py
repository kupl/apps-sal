class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        dic = {0:-1}
        # keep trace the current state of voewls
        n = 0
        res = 0
        voewls = {'a':1,'e':2,'i':4,'o':8,'u':16}
        
        for i, c in enumerate(s):
            if c in voewls:
                n ^= voewls[c]
            if n not in dic:
                dic[n] = i
            else:
                res = max(res,i - dic[n])
        return res
                
     
                

