(n, m) = map(int, input().split())
pyl = [[] for _ in range(n + 1)]
for i in range(m):
    (p, y) = map(int, input().split())
    pyl[p].append((y, i))
ans = [''] * m
for (p, yil) in enumerate(pyl):
    top = str(p).zfill(6)
    yil.sort()
    for (order, (y, i)) in enumerate(yil):
        bottom = order + 1
        bottom = str(bottom).zfill(6)
        ans[i] = top + bottom
for a in ans:
    print(a)
