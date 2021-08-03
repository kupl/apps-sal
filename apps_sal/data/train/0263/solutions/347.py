class Solution:
    def knightDialer(self, n: int) -> int:
        mod = 10**9 + 7

        if n == 1:
            return 10

        dic = {1: [6, 8], 2: [7, 9], 3: [4, 8], 4: [3, 9, 0], 6: {1, 7, 0}, 7: [2, 6], 8: [1, 3], 9: [2, 4], 0: [4, 6]}
        memo = {}

        def dfs(cur, n):
            if n == 0:
                return 1
            if (cur, n) in memo:
                return memo[cur, n]
            ret = 0
            for nxt in dic.get(cur, []):
                ret += dfs(nxt, n - 1)
            memo[cur, n] = ret
            return ret

        ret = 0
        for i in range(10):
            ret += dfs(i, n - 1)
            ret %= mod
        return ret
