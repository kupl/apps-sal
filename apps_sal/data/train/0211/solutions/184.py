class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        return self.helper(s, set())
    
    def helper(self, s, set):
        if len(s) == 1 and s in set:
            return 0
        max_split = len(set) + 1
        
        for i in range(1, len(s)):
            a = s[:i]
            b = s[i:]
            max_split = max(max_split, self.helper(b, set|{a}))
        
        return max_split
