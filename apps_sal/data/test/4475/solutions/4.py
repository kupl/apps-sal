t = int(input())
for i in range(t):
    a, b, x, y, n = [int(i) for i in input().split()]
    ans = a * b

    ck = min(a - x, n)
    ca = a - ck
    cn = n - ck
    cb = b - min(b - y, cn)
    ans = min(ans, ca * cb)

    ck = min(b - y, n)
    cb = b - ck
    cn = n - ck
    ca = a - min(a - x, cn)
    ans = min(ans, ca * cb)

    print(ans)
