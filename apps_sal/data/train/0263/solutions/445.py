class Solution:
    def knightDialer(self, n: int) -> int:
        valid = {
            1: [8, 6],
            2: [7, 9],
            3: [4, 8],
            4: [3, 9, 0],
            5: [],
            6: [1, 7, 0],
            7: [2, 6],
            8: [1, 3],
            9: [4, 2],
            0: [4, 6]
        }

        MOD = 10 ** 9 + 7
        dp = {}
        nums = 0

        def dfs(pos, steps):
            if steps == 0:
                return 1
            if (pos, steps,) in dp:
                return dp[(pos, steps,)]
            c = 0
            for next in valid[pos]:
                x = dfs(next, steps - 1)
                dp[(next, steps - 1)] = x
                c += x
                c %= MOD
            dp[(pos, steps,)] = c
            return c

        ans = 0
        for i in range(10):
            x = dfs(i, n - 1)
            ans += x
            ans %= MOD
        return ans % MOD
