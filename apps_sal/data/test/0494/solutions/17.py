R = lambda: list(map(int, input().split()))
n, m = R()
l = list(R())
a = [None] * n
c = set(range(1, n + 1))
for i in range(m - 1):
    j = l[i] - 1
    d = l[i + 1] - l[i]
    if d <= 0:
        d += n
    if a[j] != d:
        if a[j] is not None or d not in c:
            print(-1)
            return
        a[j] = d
        c.remove(d)
for i in range(n):
    if a[i] is None:
        a[i] = c.pop()
print(*a)
