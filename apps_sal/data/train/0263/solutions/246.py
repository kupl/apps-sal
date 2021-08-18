class Solution:
    def knightDialer(self, n: int) -> int:
        dic = {1: [6, 8], 2: [7, 9], 4: [0, 3, 9], 5: [], 7: [2, 6], 8: [1, 3], 0: [4, 6]}
        pair = {3: 1, 6: 4, 9: 7}

        @lru_cache(None)
        def dp(i, n):
            if n == 1:
                return 1
            if i in pair:
                i = pair[i]
            res = 0
            for j in dic[i]:
                res += dp(j, n - 1)
            return res

        return (2 * (dp(1, n) + dp(4, n) + dp(7, n)) + dp(0, n) + dp(2, n) + dp(5, n) + dp(8, n)) % (10 ** 9 + 7)
