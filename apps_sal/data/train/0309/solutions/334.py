class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        dp = {}
        ans = 0
        for i in range(len(A)):
            for j in range(i+1, len(A)):
                diff = A[i] - A[j]
                if (i, diff) in dp:
                    dp[(j, diff)] = dp[(i, diff)] + 1
                else:
                    dp[(j, diff)] = 2
                ans = max(ans, dp[(j, diff)])
        return ans

