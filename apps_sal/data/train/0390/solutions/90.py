class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        cost = [-1 for _ in range(n+1)]
        
        @lru_cache(None)
        def helper(n):
            if n == 0:
                return 0
            if cost[n] != -1:
                return cost[n]
            i = 1
            sq = 1
            while sq <= n:
                if cost[n-sq] != -1:
                    return cost[n-sq]
                if helper(n-sq) == 0:
                    cost[n-sq] = 1
                    return 1
                i += 1
                sq = i*i
            cost[n] = 0
            return 0
        
        return helper(n)

