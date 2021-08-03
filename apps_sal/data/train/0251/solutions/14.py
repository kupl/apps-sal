class Solution:
    def clumsy(self, N: int) -> int:
        fac = [0, 1, 2, 6, 7, 7, 8, 6]
        if N <= 6:
            return fac[N]

        for i in range(8, N + 1):
            temp = i * (i - 1) // (i - 2) + (i - 3) - (i - 4) * (i - 5) // (i - 6) * 2 + fac[i - 4]
            fac.append(temp)
        print(fac)
        return fac[-1]
