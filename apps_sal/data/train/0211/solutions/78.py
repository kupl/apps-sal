class Solution:

    def maxUniqueSplit(self, s: str) -> int:

        def f(s, seen):
            if not s:
                return 0
            res = 0
            for i in range(1, len(s) + 1):
                chunk = s[:i]
                if chunk not in seen:
                    res = max(res, f(s[i:], seen | {chunk}) + 1)
            return res
        return f(s, set())
