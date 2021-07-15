class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        # https://leetcode.com/problems/super-egg-drop/discuss/443089/Simplest-Python-DP-Solution-with-Detailed-Explanation-99Time-100Mem
        # M x K --> Given M moves and K eggs, what is the maximum floor we can check ?
        # M = 300 # big enough number
        # dp = [[0 for j in range(K+1)] for i in range(M+1)]
        # # Initialization 1 --> no move no floor --> dp[0][*] = 0
        # # Initialization 2 --> no egg no floor --> dp[*][0] = 0
        # # General case --> we want to find dp[m][k] --> we pick one egg and drop (1 move)
        # #              --> now we have k or k-1 eggs, depending on whether the previous egg is broken
        # #              --> so in either case, we can at least sum up 1 (first move) + dp[m-1][k] + dp[m-1][k-1] 
        # for i in range(1, M+1):
        #     for j in range(1, K+1):
        #         dp[i][j] = 1 + dp[i-1][j] + dp[i-1][j-1]
        #         if dp[i][j] >= N:
        #             return i
        memo = dict()    
        def dp(K, N):
            if K == 1:
                return N
            if N == 0:
                return 0
            if (K, N) in memo:
                return memo[(K, N)]
            res = float('inf')
            low, high = 1, N+1
            while low < high:
                mid = (low + high)//2
                broken = dp(K-1, mid -1)
                notBroken = dp(K, N-mid)
                if broken > notBroken:
                    high = mid
                    res = min(broken + 1, res)
                else:
                    low = mid + 1
                    res = min(notBroken + 1, res)    
            # for i in range(1, N+1):
            #     res = min(res, \\
            #               max(dp(K-1, i-1), dp(K, N-i))+ 1)
            memo[(K,N)] = res
            return res
        return dp(K, N)
            
                
            

