n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
a = sorted(a)
b = sorted(b)
c = sorted(c)
c.insert(0, -1)
c.append(10 ** 10)
B = [0] * n
ans = 0
for i in range(n):
    x = b[i]
    l = 0
    r = n + 1
    while r - l > 1:
        m = (l + r) // 2
        if c[m] > x:
            r = m
        elif c[m] <= x:
            l = m
    B[i] = n - l
g = [0] * n
g[n - 1] = B[n - 1]
for i in range(n - 1):
    g[-2 - i] = g[-1 - i] + B[-2 - i]
g.append(0)
b.insert(0, -1)
b.append(10 ** 10)
for i in range(n):
    x = a[i]
    l = 0
    r = n + 1
    while r - l > 1:
        m = (l + r) // 2
        if b[m] > x:
            r = m
        elif b[m] <= x:
            l = m
    ans += g[l]
print(ans)
