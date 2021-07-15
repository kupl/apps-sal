class Solution:
    def minSwap(self, A: List[int], B: List[int]) -> int:
        
        n = len(A)
        
        if n == 1:
            return 0
        
        dp = [[float('inf'), float('inf')] for _ in range(n)]
        dp[0] = [0,1] #[natural, swapped]
        
        for i in range(1, n):
            if A[i-1] < A[i] and B[i-1] < B[i]:
                dp[i] = [dp[i-1][0], dp[i-1][1]+1]
            if A[i-1] < B[i] and B[i-1] < A[i]:
                dp[i] = [min(dp[i][0],dp[i-1][1]), min(dp[i][1],dp[i-1][0]+1)]
                
        print(dp)
                

        return min(dp[-1])

