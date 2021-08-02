h, w, n = map(int, input().split())
grids = {}
D = [1, -1, 0]
for _ in range(n):
    a, b = map(int, input().split())
    a -= 1
    b -= 1

    for dx in D:
        for dy in D:
            na, nb = a + dx, b + dy
            if not(0 < na < h - 1 and 0 < nb < w - 1):
                continue
            if(na, nb) not in grids:
                grids[(na, nb)] = 0
            grids[(na, nb)] += 1


ans = [0 for _ in range(10)]

for v in grids.values():
    ans[v] += 1

ans[0] = (h - 2) * (w - 2) - sum(ans)

for a in ans:
    print(a)
