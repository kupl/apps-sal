
class Solution:
    modulo = 10**9 + 7

    def getMaxCommonFactor(self, A, B):
        while B > 0:
            A = A % B
            A, B = B, A
        return A

    def nthMagicalNumber(self, N: int, A: int, B: int) -> int:
        mcf = self.getMaxCommonFactor(A, B)
        period = (A * B // mcf) % self.modulo
        numinperiod = (A + B - mcf) // mcf
        base = N // numinperiod * period
        nums = [A * i for i in range(B // mcf)] + [B * i for i in range(1, A // mcf)]
        nums.sort()
        rem = nums[N % numinperiod]

        return (base + rem) % self.modulo
