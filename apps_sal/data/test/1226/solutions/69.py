n, a, b = map(int, input().split())

mod = 10**9 + 7

all_combi = pow(2, n, mod)


p = 1
q = 1

for i in range(b):

    p *= n - i
    p %= mod
    q *= i + 1
    q %= mod

    if i == a - 1:
        nca = p * pow(q, -1, mod) % mod

    if i == b - 1:
        ncb = p * pow(q, -1, mod) % mod


ans = all_combi - nca - ncb - 1
ans %= (10**9 + 7)

print(ans)
