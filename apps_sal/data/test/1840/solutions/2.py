from bisect import bisect_right as br
(s, b) = map(int, input().split())
a = list(map(int, input().split()))
d = [list(map(int, input().split())) for _ in range(b)]
d.sort(key=lambda f: f[0])
for i in range(1, b):
    d[i][1] += d[i - 1][1]
d = {k: v for (k, v) in d}
k = list(d.keys())
for ship in a:
    key = br(k, ship)
    ans = d[k[key - 1]] if key else 0
    print(ans, end=' ')
