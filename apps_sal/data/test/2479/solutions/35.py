n, q = map(int, input().split())
query = [list(map(int, input().split())) for _ in range(q)]

ans = (n - 2)**2
x = [n] * (n + 1)
y = [n] * (n + 1)
xm = ym = n

for a, b in query:
    if a == 1:
        if b < xm:
            y[b:xm] = [ym] * (xm - b)
            xm = b
        ans -= y[b] - 2
    else:
        if b < ym:
            x[b:ym] = [xm] * (ym - b)
            ym = b
        ans -= x[b] - 2
print(ans)
