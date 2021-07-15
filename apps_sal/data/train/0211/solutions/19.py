class Solution:
    def maxUniqueSplit(self, s: str, seen=()):
        maximum = 0
        if s:
            for i in range(1, len(s) + 1):
                candidate = s[:i]
                if candidate not in seen:
                    maximum = max(maximum, 1 + Solution.maxUniqueSplit(self, s[i:], {candidate, *seen}))
        return maximum
