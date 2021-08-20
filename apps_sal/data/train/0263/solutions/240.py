class Solution:

    def knightDialer(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        map = [[4, 6], [6, 8], [7, 9], [4, 8], [0, 3, 9], [], [0, 1, 7], [2, 6], [1, 3], [2, 4]]
        dp = [1] * len(map)
        for hops in range(n - 1):
            dp2 = [0] * len(map)
            for (node, cnt) in enumerate(dp):
                for nei in map[node]:
                    dp2[nei] += cnt
                    dp2[nei] %= MOD
            dp = dp2
        return sum(dp) % MOD
