h, w = map(int, input().split())
go = [[[] for x in range(w)] for y in range(h)]
s = input()
for i in range(h):
    if s[i] == '>':
        for j in range(w - 1):
            go[i][j].append((i, j + 1))
    else:
        for j in range(1, w):
            go[i][j].append((i, j - 1))
s = input()
for i in range(w):
    if s[i] == '^':
        for j in range(1, h):
            go[j][i].append((j - 1, i))
    else:
        for j in range(h - 1):
            go[j][i].append((j + 1, i))

good = True
for i in range(h):
    for j in range(w):
        u = [[False for x in range(w)] for y in range(h)]
        u[i][j] = True
        q = [(i, j)]
        hd = 0
        while hd < len(q):
            for g in go[q[hd][0]][q[hd][1]]:
                if not u[g[0]][g[1]]:
                    u[g[0]][g[1]] = True
                    q.append(g)
            hd += 1
        if len(q) != h * w:
            good = False


print("YES" if good else "NO")
