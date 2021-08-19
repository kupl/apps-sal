class Solution:

    def lenLongestFibSubseq(self, A: List[int]) -> int:
        N = len(A)
        index = {}
        for i in range(N):
            index[A[i]] = i
        dp = [[0] * N for _ in range(N)]
        ans = 0
        for i in range(N - 1, -1, -1):
            hi = A[i]
            for j in range(i - 1, -1, -1):
                lo = A[j]
                if hi - lo <= 0 or hi - lo >= lo:
                    break
                if hi - lo in index:
                    ind = index[hi - lo]
                    length = 1 + dp[j][i]
                    dp[ind][j] = length
                    ans = max(ans, length)
        return ans + 2 if ans > 0 else 0
