g1 = [1, 1]
g2 = [1, 1]
inverse = [0, 1]
MOD = 10**9+7
for i in range(2, 2*10**5+1):
    g1.append((g1[-1] * i) % MOD)
    inverse.append((-inverse[MOD % i] * (MOD // i)) % MOD)
    g2.append((g2[-1] * inverse[-1]) % MOD)

def comb(n, r, mod=MOD):
    if r < 0 or r > n:
        return 0
    r = min(r, n - r)
    return g1[n] * g2[r] * g2[n-r] % mod

H, W, A, B = map(int, input().split())
ans = 0
n = H + W - B - 1
for i in range(1, H-A+1):
  ans += comb(n-i, H-i) * comb(B+i-2, B-1) % MOD
  ans %= MOD

print(ans)
