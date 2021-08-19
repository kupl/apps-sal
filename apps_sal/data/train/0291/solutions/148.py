class Solution:

    def numOfSubarrays(self, arr: List[int]) -> int:
        dp = [-1 for i in range(len(arr))]
        dp[0] = [(arr[0] + 1) % 2, arr[0] % 2]
        total = dp[0][1]
        for k in range(1, len(arr)):
            if arr[k] % 2 == 0:
                dp[k] = [(dp[k - 1][0] + 1) % (10 ** 9 + 7), dp[k - 1][1] % (10 ** 9 + 7)]
                total += dp[k][1]
                total = total % (10 ** 9 + 7)
            else:
                dp[k] = [dp[k - 1][1] % (10 ** 9 + 7), (dp[k - 1][0] + 1) % (10 ** 9 + 7)]
                total += dp[k][1]
                total = total % (10 ** 9 + 7)
        return total % (10 ** 9 + 7)
