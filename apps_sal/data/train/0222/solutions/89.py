class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:
        pos = {A[i]: i for i in range(len(A))}
        dp = [[2 for j in range(len(A))] for i in range(len(A))]

        maxlen = 0
        for z in range(2, len(A)):
            for x in range(z):
                y = pos.get(A[z] - A[x], -1)
                if A[x] < (A[z] - A[x]) and y != -1:
                    dp[z][y] = dp[y][x] + 1
                    maxlen = max(maxlen, dp[z][y])

        return maxlen if maxlen > 2 else 0
