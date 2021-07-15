class Solution:
    def maxSumAfterPartitioning(self, A: List[int], K: int) -> int:    
        size = len(A)
        if K == 1: return sum(A)
        dp = [0] * (size + 1)
        for i in range(size):
            cur_max = float('-inf')
            block_size = 1
            while block_size <= K and i - block_size + 1 >= 0:
                cur_max = max(cur_max, A[i - block_size + 1])
                #cur_max = max(A[i - block_size + 1:i+1]) if i - block_size + 1 >= 0 else max(A[:i+1])
                dp[i+1] = max(dp[i+1], dp[i - block_size + 1] + block_size * cur_max)
                block_size += 1
        
        return dp[size]


