class Solution:
    def knightDialer(self, N: int) -> int:
        NEIGHBORS_MAP = {
            1: (6, 8),
            2: (7, 9),
            3: (4, 8),
            4: (3, 9, 0),
            5: tuple(),
            6: (1, 7, 0),
            7: (2, 6),
            8: (1, 3),
            9: (2, 4),
            0: (4, 6),
        }
        mx = 10**9 + 7
        memo = {}

        def dp(n, curr_num):
            if (n, curr_num) in memo:
                return memo[(n, curr_num)]

            if n == N - 1:
                return 1
            comb = 0
            for neighbor in NEIGHBORS_MAP[curr_num]:
                comb += dp(n + 1, neighbor)
            memo[(n, curr_num)] = comb
            return comb
        res = 0
        for i in range(0, 10):
            res += dp(0, i)
        return res % mx
