import bisect


class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        N = len(arr1)
        arr1 = [0] + arr1
        # 表示前 i 个元素，执行了 k 次操作后，是有序的
        dp = [[float('inf')] * (N + 1) for _ in range(N + 1)]
        dp[0][0] = -float('inf')

        arr2.sort()
        for i in range(1, N + 1):
            for k in range(i + 1):
                # 前i-1个元素，已经完成了k次交换
                if arr1[i] > dp[i - 1][k]:
                    dp[i][k] = min(dp[i][k], arr1[i])

                # 前 i-1 个元素，已经完成了 k-1次交换，所以这一次一定要交换
                if k >= 1:
                    idx_2 = bisect.bisect_right(arr2, dp[i - 1][k - 1])
                    if idx_2 != len(arr2):
                        dp[i][k] = min(dp[i][k], arr2[idx_2])

        res = float('inf')
        for i in range(1, N + 1):
            if dp[N][i] != float('inf'):
                res = min(res, i)
        return res if res != float('inf') else -1
