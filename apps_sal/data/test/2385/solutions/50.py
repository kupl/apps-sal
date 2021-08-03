N = int(input())
AB = [list(map(int, input().split())) for i in range(N - 1)]
c = [[] for i in range(N)]
for a, b in AB:
    c[a - 1].append(b - 1)
    c[b - 1].append(a - 1)
v = [1] + [0] * (N - 1)
x = [0]
s = []
parent = [-1] * N
child = [[] for i in range(N)]
while x:
    p = x.pop()
    s.append(p)
    for n in c[p]:
        if v[n] == 0:
            v[n] = 1
            x.append(n)
            parent[n] = p
            child[p].append(n)
m = 10**9 + 7
fac = [1] * (N + 10)
inv = [1] * (N + 10)
ifac = [1] * (N + 10)
for n in range(2, N + 10):
    fac[n] = (fac[n - 1] * n) % m
    inv[n] = m - inv[m % n] * (m // n) % m
    ifac[n] = (ifac[n - 1] * inv[n]) % m
size = [1] * N + [0]
dp = [1] * N + [0]
for n in s[::-1]:
    p = parent[n]
    size[p] += size[n]
    dp[n] = dp[n] * fac[size[n] - 1] % m
    dp[p] = dp[p] * ifac[size[n]] * dp[n] % m
size2 = [N - v + 1 for v in size]
dp2 = [1] * N
for n in s[1:]:
    p = parent[n]
    dp2[n] = dp[p] * ifac[size[p] - 1] * dp2[p] * ifac[size2[p] - 1] * pow(dp[n], m - 2, m) * fac[size[n]] * fac[size2[n] - 2] % m
for i in range(N):
    print(dp[i] * dp2[i] * fac[size[i] + size2[i] - 2] * ifac[size[i] - 1] * ifac[size2[i] - 1] % m)
