class Solution:
    def knightDialer(self, n: int) -> int:
        
        MOD = 10**9 + 7
        # moves: each item is numbers which can move to idx number
        # e.g., 0 can move to 4 and 6
        moves = [(4,6),(6,8),(7,9),(4,8),(3,9,0),(),
                     (1,7,0),(2,6),(1,3),(2,4)]
        
        # dp[start] = f(start, n), n as idx in dp
        # f(start, n): starting from start and dial n times
        dp = [1] * 10 
        for hops in range(n-1):
            dp2 = [0] * 10
            for node, count in enumerate(dp): # node is number
                for nei in moves[node]:
                    dp2[nei] += count
                    dp2[nei] %= MOD
            dp = dp2
        return sum(dp) % MOD
