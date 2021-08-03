class Solution:
    def maxSizeSlices(self, slices: List[int]) -> int:
        l = len(slices)
        s1 = slices[0:l - 1]
        s2 = slices[1:l]
        n = l // 3

        def summax(arr):

            dp = [[0] * (n + 1) for i in range(l + 1)]
            p = len(arr)
            for i in range(1, p + 1):
                for j in range(1, n + 1):
                    if j > i:
                        break

                    if i == 1:
                        dp[i][j] = arr[0]
                    else:
                        dp[i][j] = max(dp[i - 1][j], dp[i - 2][j - 1] + arr[i - 1])

            return dp[p][n]

        return max(summax(s1), summax(s2))
