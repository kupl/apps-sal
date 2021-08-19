class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        n = len(arr)
        dp = [[0] * 2 for _ in range(n + 1)]
        kMod = 1e9 + 7
        for i, num in enumerate(arr):

            if num & 1:
                # even
                dp[i + 1][0] = dp[i][1]
                # odd
                dp[i + 1][1] = dp[i][0] + 1
            else:
                # even
                dp[i + 1][0] = dp[i][0] + 1
                # odd
                dp[i + 1][1] = dp[i][1]

        return int(sum([dp[i][1] for i in range(n + 1)]) % kMod)
