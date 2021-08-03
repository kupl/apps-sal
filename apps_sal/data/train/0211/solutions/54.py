class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        val = 0
        if len(s) == 0:
            return val

        def helper(s, sett=()):
            return max((1 + helper(s[i:], {candidate, *sett}) for i in range(1, len(s) + 1) if (candidate := s[:i]) not in sett), default=0)
        val = helper(s)
        return val
