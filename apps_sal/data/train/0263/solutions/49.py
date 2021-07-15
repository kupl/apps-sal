class Solution:
    def knightDialer(self, n: int) -> int:
        moves = [[4,6],[6,8],[7,9],[4,8],[3,9,0],[],
                     [1,7,0],[2,6],[1,3],[2,4]]
        MOD = 10**9+7
        dp = [1]*10
        for jumps in range(n-1):
            temp = [0]*10
            for i in range(10):
                for nei in moves[i]:
                    temp[nei] += dp[i]
                    temp[nei] %= MOD
            dp = temp
        return sum(dp) % MOD

