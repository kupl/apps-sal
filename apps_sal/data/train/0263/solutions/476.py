class Solution:
    def knightDialer(self, n: int) -> int:
        def dp(cur: int, k: int, cache: dict) -> int:
            state = tuple([cur, k])
            if state in cache:
                return cache[state]

            if k == 0:
                return 1

            dic = {
                0: [4, 6],
                1: [6, 8],
                2: [7, 9],
                3: [4, 8],
                4: [0, 3, 9],
                6: [0, 1, 7],
                7: [2, 6],
                8: [1, 3],
                9: [2, 4]
            }
            res = 0
            for nc in dic.get(cur, []):
                res += dp(nc, k - 1, cache)

            cache[state] = res
            return cache[state]

        result = 0
        cache = {}
        mod = 10**9 + 7
        for i in range(10):
            result += dp(i, n - 1, cache)

        return result % (mod)
