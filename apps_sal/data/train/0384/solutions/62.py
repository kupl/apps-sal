class Solution:
    def sumSubseqWidths(self, A: List[int]) -> int:
        mod = 10**9 + 7
        n = len(A)
        if n == 1:
            return 0

        pow = [1]
        for i in range(1, n):
            pow.append(pow[-1] * 2 % mod)

        A = sorted(A)
        s = 0
        for i, elem in enumerate(A):
            n_max, n_min = i, n - i - 1
            N1 = pow[i]
            N2 = pow[n - i - 1]
            s += ((elem * (N1 - N2)) % (10**9 + 7))
            s = s % (10**9 + 7)
        return s
