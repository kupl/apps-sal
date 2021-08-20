import bisect
[n, q] = list(map(int, input().strip().split()))
ais = list(map(int, input().strip().split()))
kis = list(map(int, input().strip().split()))
iais = [0 for _ in range(n + 1)]
for i in range(n):
    iais[i + 1] = iais[i] + ais[i]
s = 0
tot = iais[-1]
r = 0
for k in kis:
    s += k
    if s >= tot:
        print(n)
        s = 0
        r = 0
    else:
        r = bisect.bisect_right(iais, s, r) - 1
        print(n - r)
