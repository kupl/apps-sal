class Solution:

    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n = len(arr)
        dp = [float('inf')] * n
        ans = float('inf')
        s = 0
        j = 0
        for i in range(n):
            s += arr[i]
            while s > target:
                s -= arr[j]
                j += 1
            if s == target:
                cur = i - j + 1
                ans = min(ans, cur + dp[j - 1])
                dp[i] = min(cur, dp[i - 1])
            else:
                dp[i] = dp[i - 1]
        return ans if ans < float('inf') else -1


"             \nclass Solution:\n    def minSumOfLengths(self, arr: List[int], target: int) -> int:\n        i, window, result = 0, 0, float('inf')\n        premin = [float('inf')] * len(arr)\n        for j, num in enumerate(arr):\n            window += num\n            while window > target:\n                window -= arr[i]\n                i += 1\n            if window == target:\n                curr = j - i + 1\n                result = min(result, curr + premin[i - 1])\n                premin[j] = min(curr, premin[j - 1])\n            else:\n                premin[j] = premin[j - 1]\n        return result if result < float('inf') else -1\n"
