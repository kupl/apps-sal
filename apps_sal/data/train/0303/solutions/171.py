class Solution:

    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        dp = [0]
        for i in range(1, len(arr) + 1):
            max_arr_num = 0
            now_max = 0
            for j in range(1, k + 1):
                idx = i - j
                if idx >= 0:
                    max_arr_num = max(max_arr_num, arr[idx])
                    now_max = max(now_max, dp[idx] + max_arr_num * j)
            dp.append(now_max)
        return dp[-1]
