n, k, d = map(int, input().split())
f, g, d, m = [0] * (n + 1), [1] * (n + 1), 1 - d, 1000000007
for i in range(1, n + 1):
    f[i] = (sum(g[j] for j in range(max(0, i - k), d + i)) + sum(f[j] for j in range(max(0, d + i), i))) % m
    g[i] = sum(g[j] for j in range(max(0, i - k), i)) % m
print(f[n])
