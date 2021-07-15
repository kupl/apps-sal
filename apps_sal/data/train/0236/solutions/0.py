class Solution:
    def minFlipsMonoIncr(self, S: str) -> int:
        onesSoFar = 0
        partial = 0
        
        for n in S:
            if n == '0':
                partial = min(onesSoFar, partial+1)      
            else:
                onesSoFar += 1
        
        return partial

