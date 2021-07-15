class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        dp = [0]*(n+1)
        for i in range(1, n+1):
            cur_max = 0
            for j in range(1, min(k, i)+1 ):
                cur_max = max(cur_max, arr[i-j])
                dp[i] = max(dp[i], cur_max*j + dp[i-j])
        return dp[-1]
                
            
        # n = len(arr)
        # memo = {n:0}
        # def helper(arr, i):
        #     if i in memo:
        #         return memo[i]
        #     res = 0
        #     for j in range(i, min(n,i+k)):
        #         res = max(res, helper(arr, j+1)+max(arr[i:j+1])*(j+1-i))
        #     memo[i] = res
        #     return res
        # return helper(arr, 0)

