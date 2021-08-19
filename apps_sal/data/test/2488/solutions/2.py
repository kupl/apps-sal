from bisect import bisect_right
(n, d, a) = map(int, input().split())
d *= 2
xh = [list(map(int, input().split())) for _ in range(n)]
xh.sort()
x = [i for (i, j) in xh] + [10 ** 20]
h = [j for (i, j) in xh]
notimos = [0] * (n + 1)
c = 0
ans = 0
for i in range(n):
    c += notimos[i]
    (xx, hh) = xh[i]
    hh = max(0, hh - c * a)
    m = 0 - -hh // a
    ans += m
    c += m
    notimos[bisect_right(x, xx + d)] -= m
print(ans)
