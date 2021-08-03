class Solution:
    def knightDialer(self, N: int) -> int:
        d = [1 for n in range(10)]
        for i in range(N - 1):
            (d[0], d[1], d[2], d[3], d[4], d[5], d[6], d[7], d[8], d[9]) = (
                d[4] + d[6], d[6] + d[8], d[7] + d[9], d[4] + d[8], d[0] + d[3] + d[9],
                0, d[0] + d[1] + d[7], d[2] + d[6], d[1] + d[3], d[2] + d[4])
        return sum(d) % (10 ** 9 + 7)
