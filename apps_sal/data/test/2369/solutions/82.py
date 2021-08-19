p = 10**9 + 7


def modpow(a, n, p):
    if n == 1:
        ans = a % p
    else:
        if n % 2 == 0:
            ans = (modpow(a, n // 2, p) ** 2) % p
        else:  # n % 2 == 1
            ans = (a * (modpow(a, n // 2, p) ** 2)) % p

    return ans


Fact = [[1, 1] for _ in range(10**5 + 1)]
for i in range(1, 10**5 + 1):
    Fact[i][0] = (Fact[i - 1][0] * i) % p
    Fact[i][1] = modpow(Fact[i][0], p - 2, p)


def C(a, b, p, Fact):
    if a < b:
        return 0
    else:
        ans = Fact[a][0] * Fact[b][1] * Fact[a - b][1] % p
        return ans


N, K = [int(x) for x in input().split()]
A = sorted([int(x) for x in input().split()])

maxS = 0
for i in range(N):
    maxS = (maxS + A[i] * C(i, K - 1, p, Fact)) % p

minS = 0
for i in range(N):
    minS = (minS + A[i] * C(N - i - 1, K - 1, p, Fact)) % p

ans = (maxS - minS) % p

print(ans)
