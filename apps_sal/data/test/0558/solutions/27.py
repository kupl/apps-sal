mod = 998244353
N, M, K = map(int, input().split())

f = 1
f_list = [1]
for m in range(1, N + 1):
    f *= m
    f %= mod
    f_list.append(f)
inv = pow(f, mod - 2, mod)    
inv_list = [1] * (N + 1)
inv_list[N] = inv

for m in range(N, 1, -1):
    inv *= m
    inv %= mod
    inv_list[m - 1] = inv

ans = 0

for i in range(K + 1):
    color = pow(M - 1, N - 1 - i, mod)
    order = f_list[N - 1] * inv_list[i] * inv_list[N - i - 1] % mod
    ans += color * order * M % mod
    ans = ans % mod
print(ans % mod)
