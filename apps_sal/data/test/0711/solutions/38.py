
class FermatCmb:
    """フェルマー小定理を使用した順列, 組み合わせ計算"""

    def __init__(self, max_num, mod):
        """
        :param max_num: max n of nCk
        :param mod: any prime number
        """
        self.max_num = max_num
        self.mod = mod
        self.fact = [0 for _ in range(max_num + 1)]
        self.factinv = [0 for _ in range(max_num + 1)]

        self.fact[0] = 1
        for i in range(1, max_num + 1):
            self.fact[i] = (i * self.fact[i - 1]) % self.mod

        self.factinv[-1] = pow(self.fact[-1], mod - 2, mod)
        for i in range(max_num, 0, -1):
            self.factinv[i - 1] = self.factinv[i] * i
            self.factinv[i - 1] %= self.mod

    def nCk(self, n, k):
        return (self.fact[n] * self.factinv[k] * self.factinv[n - k]) % self.mod

    def nPk(self, n, k):
        return (self.fact[n] * self.factinv[n - k]) % self.mod


def prime_factorization(x):
    """素因数分解"""
    import math
    re = []
    i = 2
    while x != 1:
        if x % i == 0:
            re.append(i)
            x //= i
        else:
            i += 1
            if i > math.sqrt(x):
                re.append(x)
                break
    return re


def solve(N, M):
    mod = 10 ** 9 + 7
    pf = prime_factorization(M)
    pf_map = {}
    for p in pf:
        pf_map.setdefault(p, 0)
        pf_map[p] += 1
    fc = FermatCmb(N + max(list(pf_map.values()) + [1]), mod)

    ans = 1
    for p in list(pf_map.values()):
        ans *= fc.nCk(p + N - 1, p)
        ans %= mod

    print(ans)


def __starting_point():
    N, M = list(map(int, input().split()))
    solve(N, M)


__starting_point()
