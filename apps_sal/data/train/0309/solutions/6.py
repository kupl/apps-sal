class Solution:

    def longestArithSeqLength(self, A: List[int]) -> int:
        a = len(A)
        dp = [[0] * a for _ in range(a)]
        index = [-1] * 20001
        maximum = 2
        for i in range(0, a):
            dp[i] = [2] * a
            for j in range(i + 1, a):
                first = A[i] * 2 - A[j]
                if first < 0 or index[first] == -1:
                    continue
                dp[i][j] = dp[index[first]][i] + 1
                maximum = max(maximum, dp[i][j])
            index[A[i]] = i
        return maximum
