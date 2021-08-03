class Solution:
    def consecutiveNumbersSum(self, N: int) -> int:

        total = 1  # no need to for N

        N = 2 * N

        for i in range(2, int(N**.5) + 1):  # from 2 to sqrt of N
            if N % i == 0 and ((i + (N / i)) % 2 == 1):
                total += 1

        return total
