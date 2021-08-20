import sys
input = sys.stdin.readline


def mii():
    return list(map(int, input().split()))


(n, m) = mii()
a = [[] for _ in range(n)]
c = [123456 for _ in range(n)]
for _ in range(m):
    (u, v) = mii()
    u %= n
    v %= n
    if v < u:
        v += n
    a[u].append(v)
    if c[u] > v:
        c[u] = v
ans = []
for i in list(range(1, n)) + [0]:
    out = 0
    for j in range(i, n):
        if not a[j]:
            continue
        tmp = j - i + (len(a[j]) - 1) * n + (c[j] - j)
        out = max(out, tmp)
    for j in range(i):
        if not a[j]:
            continue
        tmp = j + n - i + (len(a[j]) - 1) * n + (c[j] - j)
        out = max(out, tmp)
    ans.append(out)
print(' '.join(map(str, ans)))
