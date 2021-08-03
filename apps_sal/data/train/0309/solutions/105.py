class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        dp = [[1] * 1001 for _ in range(501)]
        res = 2
        for i, a in enumerate(A):
            flag = True
            for j in range(i):
                d = a - A[j]
                if d == 0 and not flag:
                    continue
                dp[a][d] = dp[A[j]][d] + 1
                res = max(res, dp[a][d])
                if d == 0:
                    flag = False
                # if res == dp[a][d]: print(a, d, dp[a][d])
        return res
