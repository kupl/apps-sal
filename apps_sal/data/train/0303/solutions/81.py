class Solution:
    def maxSumAfterPartitioning(self, A: List[int], K: int) -> int:
        if K == 1:
            return sum(A)
        
        # dp[i]: ans considering A[0:i]
        dp = [0] * (len(A)+1)

        for i in range(1, len(A)+1):
            cand = []
            for j in range(1, K+1):
                # consider to A[i-j:i]
                if j > i:
                    break
                temp = dp[i-j] + max(A[i-j:i]) * j
                cand.append(temp)
            
            dp[i] = max(cand)
        
        print(dp)
        return dp[-1]
