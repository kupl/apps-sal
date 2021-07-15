import bisect

class Solution:
    def makeArrayIncreasing(self, arr1, arr2) -> int:
        N = len(arr1)
        arr1 = [0] + arr1
        arr2.sort()
        dp = [[float('inf')] * (N + 1) for _ in range(N + 1)]
        dp[0][0] = -float('inf')
        
        for i in range(1, N + 1):
            for j in range(0, i + 1):
                if dp[i-1][j] < arr1[i]:
                    dp[i][j] = min(dp[i][j], arr1[i])
                if j >= 1:
                    # 要在 arr2 中找到一个比 arr1[i] 稍微大一点的数
                    idx_2 = bisect.bisect_right(arr2, dp[i-1][j-1])
                    if idx_2 != len(arr2):
                        dp[i][j] = min(dp[i][j], arr2[idx_2])
        
        # 满足条件，并且能够执行最少的次数的 K 的值
        res = float('inf')
        for i in range(1, N + 1):
            if dp[N][i] != float('inf'):
                res = min(res, i)
        return -1 if res == float('inf') else res
