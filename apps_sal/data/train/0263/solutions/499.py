class Solution:
    def knightDialer(self, n: int) -> int:
        moves = [(x, y) for x in range(-2, 3, 2) for y in range(-2, 3, 2) if abs(x) != abs(y)]
        MOD = 10 ** 9 + 7
        res = 0
        mappings = {
            1: [6, 8],
            2: [7, 9],
            3: [4, 8],
            4: [0, 3, 9],
            5: [],
            6: [0, 1, 7],
            7: [2, 6],
            8: [1, 3],
            9: [2, 4],
            0: [4, 6],
        }

        @lru_cache
        def dfs(num_jumps, cell):
            if num_jumps == 1:
                return 1
            cur = 0
            for i in mappings[cell]:
                cur += dfs(num_jumps - 1, i)
            return cur

        for i in range(0, 10):
            res += dfs(n, i)

        return res % MOD
