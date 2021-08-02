n, k = map(int, input().split())
p = 10**9 + 7


def fact(n, p):
    a = [[] for _ in range(n + 1)]
    a[0] = 1
    for i in range(n):
        a[i + 1] = (a[i] * (i + 1)) % p
    return a


f = fact(n, p)
invf = []
for i in f:
    invf.append(pow(i, -1, p))
ans = []
for i in range(1, k + 1):
    if i > n - k + 1:
        ans.append(0)
        continue
    ans.append(((f[n - k + 1] * invf[n - k + 1 - i]) % p) * ((invf[i] * f[k - 1]) % p) * ((invf[i - 1] * invf[k - i])) % p)
for i in ans:
    print(i % p)
