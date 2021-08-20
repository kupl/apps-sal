class Solution:

    def lenLongestFibSubseq(self, A: List[int]) -> int:
        if not A or len(A) == 0:
            return 0
        n = len(A)
        dp = [[0] * n for _ in range(n)]
        res = 0
        for i in range(2, n):
            l = 0
            r = i - 1
            while l < r:
                sum_ = A[l] + A[r]
                if sum_ > A[i]:
                    r -= 1
                elif sum_ < A[i]:
                    l += 1
                else:
                    dp[r][i] = dp[l][r] + 1
                    res = max(res, dp[r][i])
                    l += 1
                    r -= 1
        if res == 0:
            return 0
        return res + 2
