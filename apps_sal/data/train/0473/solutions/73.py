class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        n = len(arr)
        dp = [[0] * n for i in range(n)]

        for i in range(n):
            dp[i][i] = arr[i]

        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                dp[i][j] = dp[i][j - 1] ^ arr[j]

        output = 0
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                for k in range(i + 1, j + 1):
                    if dp[i][k - 1] == dp[k][j]:
                        output += 1

        return output
