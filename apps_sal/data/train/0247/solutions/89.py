class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n = len(arr)
        dp = [float('inf')] * (n + 1)
        s, e = 0, 0
        total = 0
        while e < n:
            total += arr[e]
            e += 1
            while total > target:
                total -= arr[s]
                s += 1
            if total == target:
                dp[e] = e - s

        ans = float('inf')
        for i in range(1, n + 1):
            if dp[i] <= i:
                ans = min(ans, dp[i - dp[i]] + dp[i])
            dp[i] = min(dp[i], dp[i - 1])

        return ans if ans < float('inf') else -1
