class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n = len(arr)
        dp = [float('inf')] * n 
        ans = float('inf'); s = 0; j = 0
        for i in range(n):
            s += arr[i]
            while s > target:
                s -= arr[j]
                j += 1
            if s == target:
                cur = i - j + 1
                ans = min(ans, cur + dp[j-1])
                dp[i] = min(cur, dp[i-1])
            else:
                dp[i] = dp[i-1]
        return ans if ans < float('inf') else -1

'''             
class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        i, window, result = 0, 0, float('inf')
        premin = [float('inf')] * len(arr)
        for j, num in enumerate(arr):
            window += num
            while window > target:
                window -= arr[i]
                i += 1
            if window == target:
                curr = j - i + 1
                result = min(result, curr + premin[i - 1])
                premin[j] = min(curr, premin[j - 1])
            else:
                premin[j] = premin[j - 1]
        return result if result < float('inf') else -1
'''
