class Solution:

    def NOD(self, a, b):
        if a == b:
            return a
        c = max(a, b)
        d = a + b - c
        c = c % d
        c = c if c > 0 else d
        return self.NOD(c, d)

    def nthMagicalNumber(self, N: int, A: int, B: int) -> int:
        const = 10 ** 9 + 7
        nod = self.NOD(A, B)
        nok = int(A * B / nod)
        (C, D) = (min(A, B), max(A, B))
        k_C = nok // C
        k_D = nok // D
        k = k_C + k_D - 1
        div = N // k
        mod = N - div * k
        k_C_cur = mod * k_C // k
        k_D_cur = mod - k_C_cur
        while True:
            C_num = k_C_cur * C
            D_num = k_D_cur * D
            if -C < C_num - D_num < D:
                return (div * nok + max(C_num, D_num)) % const
            elif C_num - D_num <= -C:
                k_D_cur -= 1
                k_C_cur += 1
            else:
                k_D_cur += 1
                k_C_cur -= 1
