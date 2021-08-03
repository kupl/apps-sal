class Solution:
    def knightDialer(self, n: int) -> int:
        if n == 1:
            return 10
        d = {0: [4, 6],
             1: [6, 8],
             2: [7, 9],
             3: [4, 8],
             4: [0, 3, 9],
             5: [],
             6: [0, 1, 7],
             7: [2, 6],
             8: [1, 3],
             9: [2, 4]
             }
        dp = [1] * 10
        for i in range(1, n):
            dp_l = [0] * 10
            for sq, count in enumerate(dp):
                for neigh in d[sq]:
                    dp_l[neigh] += count
                    dp_l[neigh] %= (10**9 + 7)

            dp = dp_l
        return sum(dp) % (10**9 + 7)
