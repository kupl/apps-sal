import sys
f = sys.stdin
(n, m) = map(int, f.readline().strip().split())
d = [{} for u in range(n)]
for i in range(m):
    (xi, yi) = map(int, f.readline().strip().split())
    d[yi - 1][xi - 1] = 1
    d[xi - 1][yi - 1] = 1


def ff(i, s):
    for k in d[i]:
        if rt[k] == 0:
            rt[k] = s
            ff(k, s)


s = 0
rt = [0 for u in range(n)]
for i in range(n):
    if rt[i] == 0:
        s += 1
        rt[i] = s
        ff(i, s)
print(2 ** (n - s))
