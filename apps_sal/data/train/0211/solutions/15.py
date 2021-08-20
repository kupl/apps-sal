class Solution:

    def maxUniqueSplit(self, s: str) -> int:

        def helper(s, seen=set()):
            maximum = 0
            for i in range(1, len(s) + 1):
                candidate = s[:i]
                if candidate not in seen:
                    maximum = max(maximum, 1 + helper(s[i:], {candidate, *seen}))
            return maximum
        return helper(s)
