class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        dp = {}
        ans = 0
        for i in range(len(A)):
            for j in range(i + 1, len(A)):
                b = A[j] - A[i]
                if (i, b) not in dp:
                    dp[(j, b)] = 2
                else:
                    dp[(j, b)] = dp[(i, b)] + 1
                ans = max(ans, dp[(j, b)])
        return ans
