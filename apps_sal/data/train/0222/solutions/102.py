class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:

        maxlen = 0
        dp = [[0 for _ in range(len(A))] for _ in range(len(A))]
        for i in range(2, len(A)):

            l, r = 0, i - 1

            while l < r:

                s = A[l] + A[r]

                if s > A[i]:
                    r -= 1
                elif s < A[i]:
                    l += 1

                else:

                    dp[r][i] = max(dp[r][i], dp[l][r] + 1)
                    maxlen = max(maxlen, dp[r][i])
                    l += 1
                    r -= 1

        return maxlen if maxlen == 0 else maxlen + 2
