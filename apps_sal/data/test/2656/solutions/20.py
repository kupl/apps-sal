def calc_inv(n, mod_n):
    inv_li = [0] * (n + 2)
    inv_li[0] = 0
    inv_li[1] = 1
    for i in range(2, n + 2):
        q, r = divmod(mod_n, i)
        inv_li[i] = -inv_li[r] * q % mod_n
    return inv_li


K = int(input())
S = input()
s_len = len(S)

MOD = 10**9 + 7
inv = calc_inv(max(K, 26) + 10, MOD)

ans = 0
p = pow(26, K, MOD)

for i in range(1, K + 2):
    ans = (ans + p % MOD) % MOD
    p = p * (s_len + i - 1) * inv[i] * 25 * inv[26] % MOD

print(ans)
