class Solution:
    def knightDialer(self, n: int) -> int:
        MOD = 10**9 + 7
        # Move records at each idex, which numbers it can jump to
        # 0 can jump to 4 and 6, 1 can jump to 6 and 8, etc
        moves = [[4,6],[6,8],[7,9],[4,8],[3,9,0],[],[1,7,0],[2,6],[1,3],[2,4]]
        dp = [1]*10
        for hops in range(n-1):
            dp2 = [0]*10
            for node, count in enumerate(dp):
                for nei in moves[node]:
                    dp2[nei] += count
                    dp2[nei] % MOD
            dp = dp2
        return sum(dp)%MOD
