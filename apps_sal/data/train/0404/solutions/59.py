class Solution:

    def largestSumOfAverages(self, A: List[int], K: int) -> float:
        n = len(A)
        averages = [[None for _ in range(n)] for _ in range(n)]
        for i in range(n):
            averages[i][i] = A[i]
        for i in range(n - 1):
            for j in range(i + 1, n):
                averages[i][j] = (averages[i][j - 1] * (j - i) + A[j]) / (j - i + 1)
        dp = [[None for _ in range(K)] for _ in range(n + 1)]

        def largestSum(i, count):
            if dp[i][count] != None:
                return dp[i][count]
            if i == n:
                dp[i][count] = 0
                return 0
            if count == K - 1:
                dp[i][count] = averages[i][n - 1]
                return averages[i][n - 1]
            largest = float('-inf')
            for k in range(n):
                largest = max(largest, averages[i][min(i + k, n - 1)] + largestSum(min(i + k + 1, n), count + 1))
            dp[i][count] = largest
            return largest
        return largestSum(0, 0)
