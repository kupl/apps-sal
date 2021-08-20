n = int(input())
a = list(map(int, input().split()))
s1 = max(1, a[0])
s2 = min(-1, a[0])
d = [0] * n
p = [0] * n
d[0] = [0, abs(a[0]) + 1][a[0] <= 0]
p[0] = [0, abs(a[0]) + 1][a[0] >= 0]
for i in range(n - 1):
    if s1 ** 2 + a[i + 1] * s1 < 0:
        d[i + 1] = d[i]
        s1 += a[i + 1]
    else:
        d[i + 1] = d[i] + abs(s1 + a[i + 1]) + 1
        s1 = [-1, 1][s1 < 0]
    if s2 ** 2 + a[i + 1] * s2 < 0:
        p[i + 1] = p[i]
        s2 += a[i + 1]
    else:
        p[i + 1] = p[i] + abs(s2 + a[i + 1]) + 1
        s2 = [-1, 1][s2 < 0]
print(min(d[n - 1], p[n - 1]))
