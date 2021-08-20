class Solution:

    def knightDialer(self, n: int) -> int:
        s = 0
        for k in range(10):
            d = [0] * 10
            d2 = [0] * 10
            d[k] = 1
            for i in range(n - 1):
                d2[0] = d[4] + d[6]
                d2[1] = d[6] + d[8]
                d2[2] = d[7] + d[9]
                d2[3] = d[4] + d[8]
                d2[4] = d[3] + d[9] + d[0]
                d2[5] = 0
                d2[6] = d[1] + d[7] + d[0]
                d2[7] = d[2] + d[6]
                d2[8] = d[1] + d[3]
                d2[9] = d[2] + d[4]
                (d, d2) = (d2, d)
            s += sum(d)
        return s % (10 ** 9 + 7)
