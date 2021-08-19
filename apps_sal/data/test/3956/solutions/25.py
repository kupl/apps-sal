class Combination:
    """
    O(n)の前計算を1回行うことで，O(1)でnCr mod mを求められる
    n_max = 10**6のとき前処理は約950ms (PyPyなら約340ms, 10**7で約1800ms)
    使用例：
    comb = Combination(1000000)
    print(comb(5, 3))  # 10
    """

    def __init__(self, n_max, mod=10 ** 9 + 7):
        self.mod = mod
        self.modinv = self.make_modinv_list(n_max)
        (self.fac, self.facinv) = self.make_factorial_list(n_max)

    def __call__(self, n, r):
        return self.fac[n] * self.facinv[r] % self.mod * self.facinv[n - r] % self.mod

    def make_factorial_list(self, n):
        fac = [1]
        facinv = [1]
        for i in range(1, n + 1):
            fac.append(fac[i - 1] * i % self.mod)
            facinv.append(facinv[i - 1] * self.modinv[i] % self.mod)
        return (fac, facinv)

    def make_modinv_list(self, n):
        modinv = [0] * (n + 1)
        modinv[1] = 1
        for i in range(2, n + 1):
            modinv[i] = self.mod - self.mod // i * modinv[self.mod % i] % self.mod
        return modinv


mod = 998244353
(K, N) = map(int, input().split())
comb = Combination(10000, mod=mod)


def C(n, r):
    if n < r or r < 0:
        return 0
    else:
        return comb(n, r)


def H(n, r):
    return C(n + r - 1, r)


L = []
for i in range(2, 2 * K + 1, 2):
    ans = 0
    M = i // 2
    b = 1
    for (j, a) in enumerate(range(M, K)):
        if M - j < 0:
            break
        ans += pow(2, M - j, mod) * C(M, j) * H(K - a, N) * b
        ans %= mod
        b = -b
    print(ans)
    if i == K + 1:
        break
    elif i == K:
        print(ans)
        print(ans)
        break
    L.append(ans)
    print(ans)
    L.append(ans)
print(*L[::-1], sep='\n')
