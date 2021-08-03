class Solution:
    def knightDialer(self, n: int) -> int:
        def dfs(pos, remain):
            if remain == 0:
                return 1
            if not (pos, remain) in memo:
                cur = 0
                for np in pos_map[pos]:
                    cur += dfs(np, remain - 1)
                memo[(pos, remain)] = cur
            return memo[(pos, remain)]

        res = 0
        memo = {}
        pos_map = {0: [4, 6], 1: [6, 8], 2: [7, 9], 3: [4, 8], 4: [0, 3, 9],
                   5: [], 6: [0, 1, 7], 7: [2, 6], 8: [1, 3], 9: [2, 4]}
        for i in range(10):
            res += dfs(i, n - 1)
        return res % (pow(10, 9) + 7)
