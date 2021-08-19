def max_unique_substrings(s, seen=()):
    return max((1 + max_unique_substrings(s[i:], {candidate, *seen}) for i in range(1, len(s) + 1) if (candidate := s[:i]) not in seen), default=0)


class Solution:

    def maxUniqueSplit(self, s: str) -> int:
        return max_unique_substrings(s)
