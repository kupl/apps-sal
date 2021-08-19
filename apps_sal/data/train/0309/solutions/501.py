class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        M = max(A) + 1
        dp = []
        for i in range(len(A)):
            temp = [1] * (M * 2)
            dp.append(temp)
        for i in range(len(A)):

            for j in range(i):
                delta = A[i] - A[j]
                k = delta + M
            #    print(k,M)
                dp[i][k] = dp[j][k] + 1
        m = 0
        for i in range(2 * M):
            for j in range(len(A)):
                m = max(dp[j][i], m)
      #  print(dp)
        return m
