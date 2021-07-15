from functools import lru_cache
class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        # return self.bottomUp(K, N)
        # return self.findMoves(K, N)
        return self.bottomUp2(K, N)
    
    @lru_cache(maxsize = None)
    def findMoves(self, K, N):
        if K == 1 or N<=1:
            return N
        
        left, right = 1, N
        while left < right:
            mid = (left + right) // 2
            
            broken = self.findMoves(K-1, mid-1)
            intact = self.findMoves(K, N-mid)
            if broken > intact:
                right = mid
            else:
                left = mid+1
        
        mid = left -1
        return 1 + max(self.findMoves(K-1, mid-1), self.findMoves(K, N-mid))

        # f = N            
        # for x in range (1, N+1):
        #     f = min(1 + max(self.findMoves(K-1, x-1), self.findMoves(K, N-x)), f)
        # return f
    
    def bottomUp(self, K, N):
        # compress to 1d array
        dp = [i for i in range(N+1)]
        for i in range(2, K+1):
            prev = dp[:]
            for j in range(1, N+1):
                min_drops = N
                for x in range(1, j+1):
                    min_drops = min(min_drops, 1 + max(prev[x-1], dp[j-x]))
                dp[j] = min_drops
        print(dp)
        return dp[N]
    
    def bottomUp2(self, K, N):
        dp = [i for i in range(N+1)]
        
        for i in range(2, K+1):
            broken = dp[1]
            for i in range(2, N+1):
                prev = dp[i]
                dp[i] = 1+dp[i-1]+broken
                broken = prev
        
        left, right = 1, N
        while left < right:
            mid = (left + right) // 2
            if dp[mid] >= N:
                right = mid
            left = left + 1
        
        return left
