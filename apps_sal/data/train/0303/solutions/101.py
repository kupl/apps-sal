# 10:28 -> misunderstood the problem
# dp
class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        dp = [0 for num in arr]
        for i in range(len(arr)):
            prev_sum = 0 if i - 1 < 0 else dp[i - 1]
            max_at_i = arr[i] + prev_sum
            possible_ks = i if i < k - 1 else k - 1
            for j in range(1, possible_ks + 1):
                current_window = arr[i - j: i + 1]
                current_max = max(current_window)
                current_window_sum = len(current_window) * current_max
                prev_window_sum = 0 if i - j - 1 < 0 else dp[i - j - 1]
                total_sum = current_window_sum + prev_window_sum
                if total_sum > max_at_i:
                    max_at_i = total_sum
            dp[i] = max_at_i
            # print(dp)
        return dp[-1]
