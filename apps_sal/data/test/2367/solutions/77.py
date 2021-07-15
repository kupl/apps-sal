class CombinationFermat:

    def __init__(self):
        """O(MAX)で前計算しておく→以降comb(a,b)はO(1)で取得可能
        """
        MOD = 10**9 + 7
        MAX = 2*10**5

        self.fac = [0]*MAX   # self.fac[n]:  (n!) mod p
        self.finv = [0]*MAX  # self.finv[n]: (n!)^-1 mod p
        self.inv = [0]*MAX   # inv[n]:  (n)^-1 mod -p
        self.fac[0] = self.fac[1] = 1
        self.finv[0] = self.finv[1] = 1
        self.inv[1] = 1
        for i in range(2, MAX):
            self.fac[i] = self.fac[i-1] * i % MOD
            self.inv[i] = MOD - self.inv[MOD % i] * (MOD//i) % MOD
            self.finv[i] = self.finv[i-1] * self.inv[i] % MOD

    def comb(self, n: int, r: int) -> int:
        MOD = 10**9 + 7
        if n < r:
            return 0
        if n < 0 or r < 0:
            return 0
        return self.fac[n] * (self.finv[r] * self.finv[n-r] % MOD) % MOD


H, W, A, B = list(map(int, input().split()))
c = CombinationFermat()
ans = 0
MOD = 10**9 + 7

for i in range(H-A):
    x = c.comb(B-1+i, i)
    a = H-1-i
    b = W-1-B
    x *= c.comb(a+b, a)
    x %= MOD
    ans += x
ans %= MOD
print(ans)

