class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        def helper(s, seen):
            return max((1 + helper(s[i:], {candidate, *seen}) for i in range(1, len(s) + 1) if (candidate := s[:i]) not in seen), default=0)
        
        
        

        rt = helper(s, set())
        return rt


          

