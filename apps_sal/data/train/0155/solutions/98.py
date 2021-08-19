class Solution:

    def maxJumps(self, arr: List[int], d: int) -> int:
        arr1 = [[i, v] for (i, v) in enumerate(arr)]
        arr1.sort(key=lambda x: x[1])
        dp = [0] * len(arr)

        def dfs(start, arr, dp):
            if dp[start] != 0:
                return dp[start]
            dp[start] = 1
            for i in range(start - 1, max(start - d - 1, -1), -1):
                if arr[start] <= arr[i]:
                    break
                dp[start] = max(dp[start], dfs(i, arr, dp) + 1)
            for i in range(start + 1, min(start + d + 1, len(arr))):
                if arr[start] <= arr[i]:
                    break
                dp[start] = max(dp[start], dfs(i, arr, dp) + 1)
            return dp[start]
        for i in range(len(arr1)):
            dfs(arr1[i][0], arr, dp)
        return max(dp)
