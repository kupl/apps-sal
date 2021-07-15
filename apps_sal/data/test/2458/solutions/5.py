t, k = map(int, input().split())
n, m = 100001, 1000000007
p, r = [0] * n, [0] * n
p[: k] = [1] * k
for i in range(k, n): p[i] = (p[i - 1] + p[i - k]) % m
for i in range(1, n): p[i] = (p[i] + p[i - 1]) % m
for i in range(t):
    a, b = map(int, input().split())
    print((p[b] - p[a - 1]) % m)
