def R():
    return list(map(int, input().split()))

n, m = R()
l = list(R())

a = [None] * n
b = [False] * n

c = set(range(1, n + 1))
for i in range(m - 1):
    j = l[i] - 1
    d = l[i + 1] - l[i]
    if d <= 0:
        d += n
    if a[j] != d:
        if a[j] is not None or b[d - 1]:
            print(-1)
            return
        a[j] = d
        b[d - 1] = True
        c.remove(d)
for i in range(n):
    if a[i] is None:
        a[i] = c.pop()
        
print(*a)

