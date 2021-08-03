class Solution:

    def count_paths(self, i, s, n, memo):

        if i < 0 or i > min(n - 1, s):

            return 0

        if s == 0 and i == 0:

            return 1

        if (s, i) in memo:

            return memo[(s, i)]

        else:

            memo[(s, i)] = self.count_paths(i - 1, s - 1, n, memo) + self.count_paths(i, s - 1, n, memo) + self.count_paths(i + 1, s - 1, n, memo)

        return memo[(s, i)]

    def numWays(self, steps: int, arrLen: int) -> int:

        memo = {}

        return self.count_paths(0, steps, arrLen, memo) % (10 ** 9 + 7)
