class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:
        n = len(A)
        max_ = 0
        dp = [[0 for i in range(n)] for j in range(n)]
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
                    max_ = max(max_, dp[r][i])
                    r -= 1
                    l += 1
        if max_ == 0:
            return 0
        else:
            return max_ + 2
