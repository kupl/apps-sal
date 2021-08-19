class Solution:

    def maxJumps(self, arr: List[int], d: int) -> int:
        N = len(arr)
        dp = [None] * N

        def cdp(i):
            if dp[i] != None:
                return dp[i]
            dp[i] = 1
            for j in range(i - 1, max(0, i - d) - 1, -1):
                if arr[j] >= arr[i]:
                    break
                dp[i] = max(dp[i], 1 + cdp(j))
            for j in range(i + 1, min(N - 1, i + d) + 1):
                if arr[j] >= arr[i]:
                    break
                dp[i] = max(dp[i], 1 + cdp(j))
            return dp[i]
        for i in range(N):
            cdp(i)
        return max(dp)
