class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        dp = [0]
        while len(dp) < k:
            dp.append(1)
            for i in range(len(dp) - 2, -1, -1):
                dp.append(dp[i] ^ 1)

        return str(dp[k - 1])
