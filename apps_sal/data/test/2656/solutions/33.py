K = int(input())
N = len(input())

mod = 10 ** 9 + 7
div = pow(26, -1, mod)
comb_i = pow(26, K, mod)
ans = comb_i
for i in range(1, K + 1):
    comb_i = (comb_i * (N - 1 + i) * pow(i, -1, mod)) % mod
    comb_i = (comb_i * 25 * div) % mod
    ans = (ans + comb_i) % mod

print(ans)
