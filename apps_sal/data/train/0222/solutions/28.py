class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:
        n = len(A)
        if n < 3:
            return 0
        dp = [[2 for j in range(n)] for i in range(n)]
        ans = 2
        hmap = {A[0]:0, A[1]:1}
        for i in range(2, n):
            for j in range(1, i):
                pos = hmap.get(A[i]-A[j], -1)
                if pos >= 0 and pos < j:
                    dp[i][j] = max(dp[i][j], dp[j][pos]+1)
                    ans = max(ans, dp[i][j])
            hmap[A[i]] = i
        return ans if ans > 2 else 0
