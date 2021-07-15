class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        return self.bt(s, set(), 0, 0)
    
   
    def bt(self, s, d, l, maxl): 
        if l >= len(s):
            maxl = max(len(d), maxl)
            return maxl
        else:
            for r in range(l+1,len(s)+1):  
                if s[l:r] not in d:   # before put the current stage into your dictionary, make sure it meet the condition. 
                    d.add(s[l:r])     # then, you have two choices: put 
                    maxl=self.bt(s, d, r, maxl)
                    d.remove(s[l:r])   # the other choice is not put. (add, then remove)
            return maxl
