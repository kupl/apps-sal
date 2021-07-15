class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        
        dp_dict = dict()
        
        def dp(K, N):
            if K == 1:
                return N
            if N == 0:
                return 0
            if (K, N) in dp_dict:
                return dp_dict[(K, N)]
            ans = inf
            
            # # normal
            # for i in range(1, N+1):
            #     ans = min(ans, max(dp(K-1, i-1), dp(K,N-i))+1)
            # dp_dict[(K, N)] = ans
            # return ans
            
            # binary
            low, high = 1, N
            while low <= high:
                mid = (high + low) // 2
                broken = dp(K-1, mid-1)
                good = dp(K, N-mid)
                if broken > good:
                    high = mid - 1
                    ans = min(broken+1, ans)
                else:
                    low = mid + 1
                    ans = min(good+1, ans)
            dp_dict[(K, N)] = ans
            return ans
            
        return dp(K, N)
