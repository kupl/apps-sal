A, B, C = map(int, input().split())
mod = 998244353
suma = ((A + 1) * A // 2) % mod
sumb = ((B + 1) * B // 2) % mod
sumc = ((C + 1) * C // 2) % mod
print((suma * sumb * sumc) % mod)
