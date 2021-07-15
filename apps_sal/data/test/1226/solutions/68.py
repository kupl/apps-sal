n, a, b = map(int, input().split())

MOD = 10 ** 9 + 7

def modinv(x, mod):
    return pow(x, mod-2, mod)

modinv_table = [-1] * (b+1)
for i in range(1, b+1):
    modinv_table[i] = modinv(i, MOD)

def comb(n, k, mod):
    ans = 1
    for i in range(k):
        ans *= n-i
        ans *= modinv_table[i + 1]
        ans %= mod
    return ans
  
ans = (pow(2, n, MOD) - comb(n, a, MOD) - comb(n, b, MOD)) % MOD - 1

print(ans)
