class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        if difference < 0:
            return self.longestSubsequence(arr[::-1], -difference)
        minim = 0
        for i in range(0, len(arr)):
            minim = min(arr[i], minim)
        maxim = arr[0]
        for i in range(0, len(arr)):
            arr[i] = arr[i] - minim
            maxim = max(maxim, arr[i])
        indices = [-1] * (maxim + difference + 1)
        dp = [0] * len(arr)
        i = len(arr) - 1
        while i >= 0:
            if indices[arr[i] + difference] != -1:
                dp[i] = 1 + dp[indices[arr[i] + difference]]
            else:
                dp[i] = 1
            indices[arr[i]] = i
            i = i - 1
        ans = -1
        for i in range(0, len(dp)):
            ans = max(ans, dp[i])
        return ans
