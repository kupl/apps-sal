class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        i = 0
        self.res = 0
        
        
        def sub(s, x):
            if len(s) == 0:
                if sorted(x) == sorted(list(set(x))):
                    self.res = max(self.res, len(set(x)))
                return

            for i in range(1, len(s)+1):
                sub(s[i:], x + [s[:i]])
            
        res = sub(s, [])
        return self.res
