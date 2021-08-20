class Solution:

    def numWays(self, steps: int, arrLen: int) -> int:
        A = [0] * (arrLen + 2)
        A[1] = 1
        mod = 10 ** 9 + 7
        for n in range(1, steps + 1):
            prev = 0
            for m in range(1, min(arrLen + 1, n + 2)):
                old = A[m]
                A[m] = (prev + A[m] + A[m + 1]) % mod
                prev = old
        return A[1]
