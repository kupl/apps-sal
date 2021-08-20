class Solution:

    def knightDialer(self, l: int) -> int:
        table = defaultdict(lambda: defaultdict(int))
        tableEnts = {(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0), (8, 0), (9, 0)}

        def dp(n, lv) -> int:
            if lv == 0:
                return 1
            if (n, lv) in tableEnts:
                return table[n][lv]
            if n == 0:
                ret = dp(4, lv - 1) + dp(6, lv - 1)
            elif n == 1:
                ret = dp(6, lv - 1) + dp(8, lv - 1)
            elif n == 2:
                ret = dp(7, lv - 1) + dp(9, lv - 1)
            elif n == 3:
                ret = dp(4, lv - 1) + dp(8, lv - 1)
            elif n == 4:
                ret = dp(3, lv - 1) + dp(9, lv - 1) + dp(0, lv - 1)
            elif n == 6:
                ret = dp(1, lv - 1) + dp(7, lv - 1) + dp(0, lv - 1)
            elif n == 7:
                ret = dp(2, lv - 1) + dp(6, lv - 1)
            elif n == 8:
                ret = dp(1, lv - 1) + dp(3, lv - 1)
            elif n == 9:
                ret = dp(2, lv - 1) + dp(4, lv - 1)
            ret %= 1000000007
            table[n][lv] = ret
            tableEnts.add((n, lv))
            return ret
        if l == 1:
            return 10
        else:
            res = 0
            for i in [0, 1, 2, 3, 4, 6, 7, 8, 9]:
                res += dp(i, l - 1)
            return res % 1000000007
