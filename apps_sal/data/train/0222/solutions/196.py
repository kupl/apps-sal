class Solution:

    def lenLongestFibSubseq(self, A: List[int]) -> int:
        candidates = set(A)
        dp = {}
        N = len(A)
        ans = 0
        for r in range(N):
            for l in range(r - 1):
                if A[l] > A[r] // 2:
                    break
                if A[r] - A[l] in candidates:
                    val = dp[A[r] - A[l], A[r]] = dp.get((A[l], A[r] - A[l]), 2) + 1
                    ans = max(ans, val)
        return ans if ans >= 3 else 0
