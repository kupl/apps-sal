class Solution:

    def maxUniqueSplit(self, s: str, seen=()) -> int:
        return max((1 + self.maxUniqueSplit(s[i:], {candidate, *seen}) for i in range(1, len(s) + 1) if (candidate := s[:i]) not in seen), default=0)
