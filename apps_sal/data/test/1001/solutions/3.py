n = int(input())
a = [0] + list(map(int, input().split()))
p = [0]
for i in range(1, n + 1):
    p += [p[-1] + a[i]]
d = [p[n]] * (n + 1)

for i in range(n - 2, 0, -1):
    d[i] = max(d[i + 1], p[i + 1] - d[i + 1])

print(d[1])
