class Solution:

    def maxSizeSlices(self, slices: List[int]) -> int:
        self.slices = slices
        n = len(self.slices)
        self.mem = dict()
        rv1 = self.dfs(1, n - 1, n // 3)
        rv2 = self.dfs(0, n - 2, n // 3)
        return max(rv1, rv2)

    def dfs(self, i, j, k):
        if k <= 0:
            return 0
        if j - i + 1 < 2 * k - 1:
            return -float('inf')
        key = (i, j, k)
        if key in self.mem:
            return self.mem[key]
        rv = max(self.dfs(i + 1, j, k), self.slices[i] + self.dfs(i + 2, j, k - 1))
        self.mem[key] = rv
        return rv
