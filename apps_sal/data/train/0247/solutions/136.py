class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        # They are all positive

        n = len(arr)
        # DP is shortest array up to i
        dp = [float('inf') for _ in range(n + 1)]

        ans = float('inf')

        start = 0

        curr_sum = 0
        for end in range(n):
            curr_sum += arr[end]

            while start < end and curr_sum > target:
                curr_sum -= arr[start]
                start += 1

            if curr_sum == target:
                print(start, end)
                ans = min(ans, end - start + 1 + dp[start - 1])  # or start - 1
                dp[end] = min(dp[end - 1], end - start + 1)
            else:
                dp[end] = dp[end - 1]

        print(dp)
        return ans if ans != float('inf') else -1
