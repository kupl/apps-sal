from bisect import bisect_right
n, k = map(int, input().split())
t = sorted((u - k * v, v) for u, v in zip(*(map(int, input().split()), map(int, input().split()))))
m = n - bisect_right(t, (0, 0))
l, p, t = 0, [0] * 100001, t[:: -1]
for d, v in t[: m]:
    for j in range(l, 0, -1):
        if p[j]:
            p[j + d] = max(p[j + d], p[j] + v)
    p[d] = max(p[d], p[0] + v)
    l += d
for d, v in t[m:]:
    for j in range(- d, l + 1):
        if p[j]:
            p[j + d] = max(p[j + d], p[j] + v)
print(p[0] * k if p[0] else -1)
