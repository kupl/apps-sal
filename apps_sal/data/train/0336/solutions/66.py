class Solution:
    def minSteps(self, s: str, t: str) -> int:
        
        count = 0
        for ch2 in set(s):
            n = s.count(ch2)
            m = t.count(ch2)
            if(ch2 in t):
               if(m < n):
                  count += n - m
            else:
                count += n
        return count 

