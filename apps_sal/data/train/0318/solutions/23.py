class Solution:
    def dp(self, i, j, k, l):
        # max by taking k from s[i:j] assume cycle if l = 1 else no-cycle
        if (i, j, k, l) not in self.memo:
            if k == 1:
                self.memo[(i, j, k, l)] = max(self.s[i:j])
            elif j - i < 2 * k - 1:
                self.memo[(i, j, k, l)] = float('-inf')
            else:
                # max of taking self.s[i] and not taking self.s[i] at this step
                self.memo[(i, j, k, l)] = max(self.dp(i + 2, j - l, k - 1, 0) + self.s[i], self.dp(i + 1, j, k, 0))
        return self.memo[(i, j, k, l)]

    def maxSizeSlices(self, slices: List[int]) -> int:
        # Q0213, dynamic programming
        self.memo, self.s, n = {}, slices, len(slices)
        return self.dp(0, n, n // 3, 1)
