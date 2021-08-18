r, p = range, print
n, a, b = map(int, input().split())
if a + b > n + 1 or a * b < n:
    print(-1)
    return
l = [[]for i in r(b - 1)] + [list(r(1, a + 1))]
for i in r(a, n):
    l[-2 - (i - a) % (b - 1)] += [i + 1]
for i in l:
    p(*i, end=" ")
