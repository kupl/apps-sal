class Solution:

    def longestArithSeqLength(self, A: List[int]) -> int:
        if len(A) < 2:
            return 0
        la = len(A)
        dp = {}
        curr = 0
        for i in range(1, la):
            for j in range(i):
                d = A[i] - A[j]
                dp[i, d] = dp.get((j, d), 1) + 1
                if dp[i, d] > curr:
                    curr = dp[i, d]
        return curr
