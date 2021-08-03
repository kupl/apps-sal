class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        def builder(s, seen):
            if not s:
                return 0

            res = 0
            for i, c in enumerate(s):
                candidate = s[:i + 1]
                if candidate not in seen:
                    seen.add(candidate)
                    res = max(res, 1 + builder(s[i + 1:], seen))
                    seen.remove(candidate)

            return res

        return builder(s, set())
