n, m, d = list(map(int, input().split()))
a = []
for i in range(n):
    b = list(map(int, input().split()))
    a = a + b
a.sort()
if d > a[n * m - 1] - a[0] and a[0] != a[n * m - 1]:
    print(-1)
else:
    s = 0
    x = a[0] % d
    m = a[n * m // 2]
    for i in a:
        if i % d != x:
            print(-1)
            return
        s = s + abs(m - i) / d
    print(int(s))
