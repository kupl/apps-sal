class Solution:

    def maxUniqueSplit(self, s: str) -> int:

        def max_uni_seq(s, vis=()):
            return max((1 + max_uni_seq(s[i:], {sol, *vis}) for i in range(1, len(s) + 1) if (sol := s[:i]) not in vis), default=0)
        return max_uni_seq(s)
