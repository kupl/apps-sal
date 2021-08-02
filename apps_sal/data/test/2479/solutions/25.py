n, q = list(map(int, input().split()))
ans = (n - 2)**2

d = [n] * (n + 1)
r = [n] * (n + 1)

rmin = n
dmin = n

for _ in range(q):
    query, x = list(map(int, input().split()))
    if query == 1:
        if x < rmin:
            for i in range(rmin, x - 1, -1):
                r[i] = dmin
            rmin = x
        ans -= r[x] - 2

    else:
        if x < dmin:
            for i in range(dmin, x - 1, -1):
                d[i] = rmin
            dmin = x
        ans -= d[x] - 2

print(ans)
