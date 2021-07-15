class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:
        dp = dict()
        res = 2
        for i in range(len(A)):
            for j in range(i):
                if (A[j], A[i]-A[j]) in dp:
                    dp[A[i], A[j]] = dp[A[j], A[i]-A[j]] + 1
                else:
                    dp[A[i], A[j]] = 2
                
                res = max(res, dp[A[i], A[j]])
                
        return res if res > 2 else 0

