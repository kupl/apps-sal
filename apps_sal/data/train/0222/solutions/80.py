class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:
        n = len(A)
        if n < 3:
            return 0

        dp = [[2 for j in range(n)] for i in range(n)]
        ans = 2
        for i in range(2, n):
            l, r = 0, i - 1
            while l < r:
                if A[l] + A[r] == A[i]:
                    dp[i][r] = max(dp[i][r], dp[r][l] + 1)
                    ans = max(ans, dp[i][r])
                    l += 1
                    r -= 1
                elif A[l] + A[r] < A[i]:
                    l += 1
                else:
                    r -= 1
        return ans if ans > 2 else 0
