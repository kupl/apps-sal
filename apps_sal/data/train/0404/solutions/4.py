class Solution:
    def largestSumOfAverages(self, A, K: int) -> float:
        A = [0] + A
        len_a = len(A)
        dp = [[0] * (K+1) for _ in range(len_a)]
        
        for i in range(1, len_a):
            dp[i][0] = -float('inf')
        
        for i in range(1, len_a):
            for k in range(1, min(K+1, i+1)):
                for j in range(k, i+1):
                    dp[i][k] = max(dp[i][k], dp[j-1][k-1] + self.helper(A[j:i+1]))
        return dp[-1][-1]
    
    def helper(self, sub_a):
        return sum(sub_a) / len(sub_a)
