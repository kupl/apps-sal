from math import gcd


def divisors(M):  # Mの約数列 O(n^(0.5+e))
    d = []
    i = 1
    while M >= i**2:
        if M % i == 0:
            d.append(i)
            if i**2 != M:
                d.append(M // i)
        i = i + 1
    d.sort()
    return d


mod = 10**9 + 7
N, K = list(map(int, input().split()))
div = divisors(N)

res = [0 for i in range(len(div))]
ans = 0
if N % 2 == 0:
    for i in range(len(div)):
        d = div[i]
        g = gcd(2 * d, N)
        res[i] += pow(K, g // 2, mod)
        res[i] %= mod
        ans += d * res[i]
        ans %= mod
        for j in range(i + 1, len(div)):
            if div[j] % d == 0:
                res[j] -= res[i]
                res[j] %= mod

    print((ans % mod))
else:
    for i in range(len(div)):
        d = div[i]
        g = gcd(2 * d, N)
        res[i] += pow(K, (g + 1) // 2, mod)
        res[i] %= mod
        ans += d * res[i]
        ans %= mod
        for j in range(i + 1, len(div)):
            if div[j] % d == 0:
                res[j] -= res[i]
                res[j] %= mod

    print((ans % mod))
