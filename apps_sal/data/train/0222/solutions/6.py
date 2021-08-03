class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        n = len(arr)
        dic = {arr[i]: i for i in range(n)}
        ans = 2
        dp = [[2] * n for _ in range(n)]

        for k in range(n):
            for j in range(k):
                i = dic.get(arr[k] - arr[j], None)
                if i is not None and j > i:
                    dp[j][k] = dp[i][j] + 1
                    ans = max(ans, dp[j][k])
        if ans == 2:
            return 0
        return ans
