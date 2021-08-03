class Solution:
    splits = set()

    def maxUniqueSplit(self, s: str) -> int:
        n = len(s)
        result = 0

        for i in range(1, n + 1):
            current = s[:i]
            if current not in self.splits:
                self.splits.add(current)
                result = max(result, 1 + self.maxUniqueSplit(s[i:]))
                self.splits.remove(current)

        return result
