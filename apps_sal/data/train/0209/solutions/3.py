class Solution:

    def mergeStones(self, stones: List[int], K: int) -> int:
        n = len(stones)
        k = K
        if n < k and n != 1 or (n - 1) % (k - 1) != 0:
            return -1
        if n == 1:
            return 0
        dp = [[-1 for _ in range(n)] for _ in range(n)]
        self.solve(stones, 0, n - 1, k, dp)
        return dp[0][n - 1]

    def solve(self, stones, l, r, k, dp):
        length = r - l + 1
        if length < k:
            dp[l][r] = 0
            return
        if length == k:
            dp[l][r] = sum(stones[l:r + 1])
            return
        res = float('inf')
        for m in range(l, r):
            length = length
            length_l = m - l + 1
            length_r = r - m
            rem = k - 1 if length % (k - 1) == 0 else length % (k - 1)
            rem_l = k - 1 if length_l % (k - 1) == 0 else length_l % (k - 1)
            rem_r = k - 1 if length_r % (k - 1) == 0 else length_r % (k - 1)
            rem_total = k - 1 if (rem_l + rem_r) % (k - 1) == 0 else (rem_l + rem_r) % (k - 1)
            if rem_total == rem and rem_l + rem_r <= k:
                if dp[l][m] == -1:
                    self.solve(stones, l, m, k, dp)
                if dp[m + 1][r] == -1:
                    self.solve(stones, m + 1, r, k, dp)
                res = min(res, dp[l][m] + dp[m + 1][r])
        dp[l][r] = res
        if rem == 1:
            dp[l][r] += sum(stones[l:r + 1])
