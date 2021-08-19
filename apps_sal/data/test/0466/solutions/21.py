(c, d) = map(int, input().split())
(n, m) = map(int, input().split())
k = int(input())
f = [float('+inf') for i in range(n * m + n + k + 2)]
f[0] = f[k] = 0
for i in range(n * m):
    f[i + 1] = min(f[i + 1], f[i] + d)
    f[i + n] = min(f[i + n], f[i] + c)
print(min(f[n * m:]))
