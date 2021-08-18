class Solution:
    def dp(self, i, j, k, l):
        if (i, j, k, l) not in self.memo:
            if k == 1:
                self.memo[(i, j, k, l)] = max(self.s[i:j])
            elif j - i < 2 * k - 1:
                self.memo[(i, j, k, l)] = float('-inf')
            else:
                self.memo[(i, j, k, l)] = max(self.dp(i + 2, j - l, k - 1, 0) + self.s[i], self.dp(i + 1, j, k, 0))
        return self.memo[(i, j, k, l)]

    def maxSizeSlices(self, slices: List[int]) -> int:
        self.memo, self.s, n = {}, slices, len(slices)
        return self.dp(0, n, n // 3, 1)
