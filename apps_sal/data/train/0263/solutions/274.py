class Solution:
    def knightDialer(self, n: int) -> int:
        s = 0
        for k in range(10):
            d = [0] * 10
            d[k] = 1
            for i in range(n - 1):
                d2 = [
                    d[4] + d[6],
                    d[6] + d[8],
                    d[7] + d[9],
                    d[4] + d[8],
                    d[3] + d[9] + d[0],
                    0,
                    d[1] + d[7] + d[0],
                    d[2] + d[6],
                    d[1] + d[3],
                    d[2] + d[4],
                ]
                d = d2
            s += sum(d)
        return s % (10 ** 9 + 7)


