class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        dp = {}
        N = len(A)
        for i in range(N):
            for j in range(i + 1, N):
                dp[j, A[j] - A[i]] = dp.get((i, A[j] - A[i]), 1) + 1
        return max(dp.values())
        # def calc(A):
        #     for i in range(len(A) - 1, -1, -1):
        #         for j in range(i + 1, len(A)):
        #             if A[j] < A[i]:
        #                 continue
        #             diff = A[j] - A[i]
        #             memo[i][diff] = max(memo[i].get(diff, 0), memo[j].get(diff, 1) + 1)
        #             ret = max(ret, memo[i][diff])
        #     return ret
        #
        # return max(
        #     calc(A), calc(list(reversed(A)))
        # )
