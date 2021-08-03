class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        n = len(A)
        dp = {}
        ans = 0
        for i in range(n):
            for j in range(i):
                diff = A[i] - A[j]
                if (diff, j) not in dp:

                    dp[(diff, i)] = 2
                else:

                    dp[(diff, i)] = dp[(diff, j)] + 1
                ans = max(ans, dp[(diff, i)])
        return ans
