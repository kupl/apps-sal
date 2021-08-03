class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        self.memo = [[[0 for k in range(16)] for j in range(6)] for i in range(5001)]

        def helper(n, prev, m):
            if n == 0:
                return 1
            if self.memo[n][prev][m] > 0:
                return self.memo[n][prev][m]
            ans = 0
            for i in range(6):
                if prev == i:
                    if m >= rollMax[i]:
                        continue

                    ans += helper(n - 1, i, m + 1)
                else:
                    ans += helper(n - 1, i, 1)
            self.memo[n][prev][m] = ans
            return ans
        return helper(n, -1, 0) % (10**9 + 7)
