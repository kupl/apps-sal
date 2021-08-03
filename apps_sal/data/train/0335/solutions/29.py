class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        rods.sort(reverse=True)
        n = len(rods)
        dp = [0 for i in range(n)]
        rsum = 0
        self.result = 0

        for i in range(n - 1, -1, -1):
            rsum += rods[i]
            dp[i] = rsum

        def dfs(idx, lsum, rsum):
            if idx >= n:
                if lsum == rsum:
                    self.result = max(self.result, lsum)
                return

            if abs(lsum - rsum) > dp[idx]:
                return
            if lsum + rsum + dp[idx] <= 2 * self.result:
                return

            dfs(idx + 1, lsum + rods[idx], rsum)
            dfs(idx + 1, lsum, rsum + rods[idx])
            dfs(idx + 1, lsum, rsum)

        dfs(0, 0, 0)
        return self.result
