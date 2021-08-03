import sys
sys.setrecursionlimit(10**9)


class Combination:
    def __init__(self, n_max, mod=10**9 + 7):
        self.mod = mod
        self.modinv = self.make_modinv_list(n_max)
        self.fac, self.facinv = self.make_factorial_list(n_max)

    def __call__(self, n, r):
        return self.fac[n] * self.facinv[r] % self.mod * self.facinv[n - r] % self.mod

    def make_factorial_list(self, n):
        # 階乗のリストと階乗のmod逆元のリストを返す O(n)
        # self.make_modinv_list()が先に実行されている必要がある
        fac = [1]
        facinv = [1]
        for i in range(1, n + 1):
            fac.append(fac[i - 1] * i % self.mod)
            facinv.append(facinv[i - 1] * self.modinv[i] % self.mod)
        return fac, facinv

    def make_modinv_list(self, n):
        # 0からnまでのmod逆元のリストを返す O(n)
        modinv = [0] * (n + 1)
        modinv[1] = 1
        for i in range(2, n + 1):
            modinv[i] = self.mod - self.mod // i * modinv[self.mod % i] % self.mod
        return modinv


N, K = map(int, input().split())
adj = [[]for _ in range(N)]
comb = Combination(10**5)


def nPr(n, r):
    if n < r:
        return 0
    return comb(n, r) * comb.fac[r]


for _ in range(N - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    adj[a].append(b)
    adj[b].append(a)


def dfs(v, p=-1):
    nonlocal ans
    c = 0
    for nei in adj[v]:
        if nei == p:
            continue
        c += 1
        dfs(nei, v)

    nk = K - 1 if p == -1 else K - 2
    ans *= nPr(nk, c)
    ans %= 10**9 + 7


ans = K
dfs(0)
print(ans)
