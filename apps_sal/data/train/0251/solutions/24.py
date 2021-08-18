class Solution:
    def clumsy(self, N: int) -> int:

        res = 0
        for i in range(N, 0, -4):
            if i >= 4:
                if i == N:
                    res += i * (i - 1) // (i - 2) + (i - 3)
                else:
                    res -= i * (i - 1) // (i - 2) - (i - 3)

        neg = [1, -1][int(N >= 4)]

        if N % 4 == 3:
            res += 6 * neg
        elif N % 4 == 2:
            res += 2 * neg
        elif N % 4 == 1:
            res += 1 * neg
        return int(res)
