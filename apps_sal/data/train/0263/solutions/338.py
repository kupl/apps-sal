move_map = {0: {4, 6}, 1: {6, 8}, 2: {7, 9}, 3: {4, 8}, 4: {3, 9, 0}, 5: {}, 6: {1, 0, 7}, 7: {2, 6}, 8: {1, 3}, 9: {2, 4}}


class Solution:

    def dfs(self, n, key):
        if n == 1:
            return 1
        if (n, key) in self.memo:
            return self.memo[n, key]
        res = 0
        for new_key in move_map[key]:
            res += self.dfs(n - 1, new_key)
        self.memo[n, key] = res
        return res

    def knightDialer(self, n: int) -> int:
        self.memo = {}
        res = 0
        for key in move_map:
            res += self.dfs(n, key)
        return res % (10 ** 9 + 7)
