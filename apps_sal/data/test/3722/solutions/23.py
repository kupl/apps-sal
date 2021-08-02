class comb():
    F = [1, 1]
    Fi = [1, 1]
    I = [0, 1]

    def __init__(self, num, mod):
        self.MOD = mod
        for i in range(2, num + 1):
            self.F.append((self.F[-1] * i) % mod)
            self.I.append(mod - self.I[mod % i] * (mod // i) % mod)
            self.Fi.append(self.Fi[-1] * self.I[i] % mod)

    def com(self, n, k):
        if n < k: return 0
        if n < 0 or k < 0: return 0
        return self.F[n] * (self.Fi[k] * self.Fi[n - k] % self.MOD) % self.MOD


N = int(input())
caa = input()
cab = input()
cba = input()
cbb = input()
MOD = 10 ** 9 + 7

if (cab == "A" and caa == "A") or (cab == "B" and cbb == "B"):
    print((1))
    return

com = comb(N, MOD)
if cab == cba:
    ans = 0
    for n in range((N - 2) // 2 + 1):
        m = N - 2 - n
        if m < n: continue
        ans = (ans + com.com(m, n)) % MOD
    print(ans)
    return

if N <= 3:
    print((1))
else:
    ans = pow(2, N - 3, MOD)
    print(ans)
