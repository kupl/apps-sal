class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        inf = 0x3f3f3f3f
        dp = [[(-inf, -inf) for _ in range(k+1)] for _ in range(len(arr)+1)]
        last_max = 0
        dp[0][0] = (0, 0)
        for i in range(1, len(arr) + 1):
            for j in range(1, k + 1):
                if j == 1:
                    dp[i][j] = (last_max + arr[i-1], arr[i-1])
                    last_max = dp[i][j][0]
                elif i >= j:
                    last_s, last_n = dp[i-1][j-1]
                    n = max(last_n, arr[i-1])
                    s = last_s - last_n * (j-1) + n * j
                    dp[i][j] = (s, n)
                    last_max = max(last_max, s)
            #    print(i, j, dp[i][j])
        return last_max
