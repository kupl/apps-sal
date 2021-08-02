n, m = list(map(int, input().split()))
grid = []
sloc = (-1, -1)
eloc = (-1, -1)
for y in range(n):
    l = input()
    grid.append(list())
    for x in range(m):
        grid[-1].append(l[x] == '#')
        if l[x] == 'S':
            sloc = (x, y)
        elif l[x] == 'E':
            eloc = (x, y)

pb = []
for a in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
    for b in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        for c in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            for d in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                if len(set([a, b, c, d])) == 4 and [a, b, c, d] not in pb:
                    pb.append([a, b, c, d])

s = input()

ans = 0
for mp in pb:
    seen = False
    works = True
    loc = sloc
    for j in s:
        j = int(j)
        if seen:
            break
        if not works:
            break
        nloc = (loc[0] + mp[j][0], loc[1] + mp[j][1])
        if min(nloc) < 0 or nloc[0] >= m or nloc[1] >= n:
            works = False
            break
        if grid[nloc[1]][nloc[0]]:
            works = False
            break
        if nloc == eloc:
            seen = True
            break
        loc = nloc
    if seen:
        ans += 1

print(ans)
