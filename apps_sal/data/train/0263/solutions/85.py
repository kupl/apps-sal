class Solution:
    def knightDialer(self, n: int) -> int:
        #         mod = 10**9 + 7

        #         d = dict()
        #         d[0] = {4, 6}
        #         d[1] = {6, 8}
        #         d[2] = {7, 9}
        #         d[3] = {4, 8}
        #         d[4] = {0, 3, 9}
        #         d[6] = {0, 1, 7}
        #         d[7] = {2, 6}
        #         d[8] = {1, 3}
        #         d[9] = {2, 4}

        #         memo = [[0]*10 for i in range(n+1)]
        #         memo[1] = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

        #         for i in range(2, n+1):
        #             for key, val in d.items():
        #                 for v in val:
        #                     memo[i][key] += memo[i-1][v]

        #         return sum(memo[-1])%mod

        MOD = 10**9 + 7
        moves = [[4, 6], [6, 8], [7, 9], [4, 8], [3, 9, 0], [],
                 [1, 7, 0], [2, 6], [1, 3], [2, 4]]

        dp = [1] * 10
        for hops in range(n - 1):
            dp2 = [0] * 10
            for node, count in enumerate(dp):
                for nei in moves[node]:
                    dp2[nei] += count
                    dp2[nei] %= MOD
            dp = dp2
        return sum(dp) % MOD
