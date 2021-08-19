n, m, p = map(int, input().split())
s = list(map(int, input().split()))
a = []
front = [set() for i in range(p)]
for i in range(n):
    a.append([(int(0) if ch == '.' else (-1 if ch == '#' else (int(ch) if not front[int(ch) - 1].add((i, j)) else -99))) for j, ch in enumerate(input())])

move = [(-1, 0), (1, 0), (0, -1), (0, 1)]
i = 0
blocked = [False] * p
activeplayers = p

i = 0
while activeplayers > 0:
    if blocked[i]:
        i = (i + 1) % p
        continue
    aset = front[i]
    mademove = False
    for gtime in range(s[i]):
        newset = set()
        for x, y in aset:
            for dx, dy in move:
                if 0 <= x + dx < n and 0 <= y + dy < m:
                    if a[x + dx][y + dy] == 0:
                        newset.add((x + dx, y + dy))
                        a[x + dx][y + dy] = (i + 1)
                        mademove = True
        aset = newset
        if len(aset) == 0:
            mademove = False
            break
    front[i] = aset
    if not mademove:
        blocked[i] = True
        activeplayers = activeplayers - 1
    i = (i + 1) % p

res = [0] * p


for i in range(n):
    for j in range(m):
        if a[i][j] > 0:
            res[int(a[i][j]) - 1] = res[int(a[i][j]) - 1] + 1

for i in range(p):
    print(res[i], end=' ')
