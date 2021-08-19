class Solution:

    def consecutiveNumbersSum(self, N: int) -> int:
        sol = 0
        m = 1
        while m * (m + 1) < 2 * N:
            a = (1.0 * N - m * (m + 1) / 2) / (m + 1)
            if a - int(a) == 0.0:
                sol += 1
            m += 1
        return sol + 1
