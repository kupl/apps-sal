mod = 998244353


def nCrModp(n, r):
    C = [0 for i in range(r + 1)]
    C[0] = 1
    for i in range(1, n + 1):
        for j in range(min(i, r), 0, -1):
            C[j] = (C[j] + C[j - 1]) % mod
    return C[r]


(n, m, k) = map(int, input().split())
if m == 1 and k > 0:
    print(0)
else:
    ans = m
    ans = ans % mod * (pow(m - 1, k, mod) % mod) % mod
    val1 = nCrModp(n - 1, k)
    ans = ans % mod * (val1 % mod) % mod
    print(ans)
