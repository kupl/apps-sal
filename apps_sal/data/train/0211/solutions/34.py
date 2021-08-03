class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        self._s = s
        self.best = 1

        self.solve(0, set(), 0)
        return self.best

    def solve(self, index, seen, count):
        s = self._s

        if index >= len(s):
            self.best = max(self.best, count)

        for end in range(index + 1, len(s) + 1):
            if s[index:end] not in seen:
                seen.add(s[index:end])
                self.solve(end, seen, count + 1)
                seen.remove(s[index:end])
