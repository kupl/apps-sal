class Solution:

    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n = len(arr)
        left_presum = {0: 0}
        left_dp = [float('inf')] * (n + 1)
        total = 0
        for i in range(1, n + 1):
            total += arr[i - 1]
            if total - target in left_presum:
                left_dp[i] = min(i - left_presum[total - target], left_dp[i - 1])
            else:
                left_dp[i] = left_dp[i - 1]
            left_presum[total] = i
        total = 0
        right_presum = {0: n}
        right_dp = [float('inf')] * (n + 1)
        for i in range(n - 1, -1, -1):
            total += arr[i]
            if total - target in right_presum:
                right_dp[i] = min(right_dp[i + 1], right_presum[total - target] - i)
            else:
                right_dp[i] = right_dp[i + 1]
            right_presum[total] = i
        print(right_dp)
        ans = float('inf')
        for i in range(1, n):
            if left_dp[i] == float('inf') or right_dp[i] == float('inf'):
                continue
            ans = min(ans, left_dp[i] + right_dp[i])
        return -1 if ans == float('inf') else ans
