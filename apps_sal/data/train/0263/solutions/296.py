class Solution:

    def knightDialer(self, n: int) -> int:
        """
        mod = 10**9 + 7
        moves = [[4,6],[6,8],[7,9],[4,8],[3,9,0],[],[1,7,0],[2,6],[1,3],[2,4]]
        dp = [1]*10
        for _ in range(n-1):
            dp2 = [0]*10
            for node, count in enumerate(dp):
                for nei in moves[node]:
                    dp2[nei] = (dp2[nei] + count) % mod
            dp = dp2
        return sum(dp)%mod
        """
        mod = 10 ** 9 + 7
        x0 = x1 = x2 = x3 = x4 = x5 = x6 = x7 = x8 = x9 = 1
        for k in range(1, n):
            (x0, x1, x2, x3, x4, x5, x6, x7, x8, x9) = (x4 + x6, x6 + x8, x7 + x9, x4 + x8, x3 + x9 + x0, 0, x1 + x7 + x0, x2 + x6, x1 + x3, x2 + x4)
        return (x0 + x1 + x2 + x3 + x4 + x5 + x6 + x7 + x8 + x9) % mod
