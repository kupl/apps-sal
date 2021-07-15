H,W,A,B = list(map(int,input().split()))


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

comb = Combination(1000000)
MOD = 10**9+7
ans = 0
for i in range(B,W):
    ans += comb(H-A-1+i,i)*comb(A-1+W-1-i,A-1)
    ans %= MOD
    #print(comb(H-A-1+i,i)*comb(A-1+W-1-i,A-1))
print(ans)



