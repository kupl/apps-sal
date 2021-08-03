class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        def max_unique(s, visited=()):
            return max((1 + max_unique(s[i:], {candidate, *visited}) for i in range(1, len(s) + 1) if (candidate := s[:i]) not in visited), default=0)
        return max_unique(s)
