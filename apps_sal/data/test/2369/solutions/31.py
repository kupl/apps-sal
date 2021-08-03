N, K = map(int, input().split())
p = 10**9 + 7
f = [1]
for i in range(1, N + 1):
    f.append(f[-1] * i % p)


def nCk(n, k):
    return f[n] * pow(f[n - k], p - 2, p) * pow(f[k], p - 2, p)


a = list(map(int, input().split()))
a.sort()

ans = 0
for i in range(N - K + 1):
    ans -= (a[i] * nCk(N - i - 1, K - 1)) % p
    ans += (a[N - i - 1] * nCk(N - i - 1, K - 1)) % p
print(ans % p)
