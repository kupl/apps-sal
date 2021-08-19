class Solution:

    def knightDialer(self, n: int) -> int:
        if n == 1:
            return 10
        c = [1, 2, 2, 4]
        nx = [0, 0, 0, 0]
        for i in range(n - 1):
            nx[0] = c[1]
            nx[1] = 2 * c[0] + c[3]
            nx[2] = c[3]
            nx[3] = 2 * (c[1] + c[2])
            c = nx[:]
        return sum(c) % (10 ** 9 + 7)
