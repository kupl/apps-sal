q = int(input())
for _ in range(q):
    r, c = list(map(int, input().split()))

    def nbr(x, y):
        out = []
        if x < r - 1:
            out.append([x + 1, y])
        if x > 0:
            out.append([x - 1, y])
        if y > 0:
            out.append([x, y - 1])
        if y < c - 1:
            out.append([x, y + 1])
        return out
    mat = [list(input()) for i in range(r)]
    # print(mat)
    for x in range(r):
        for y in range(c):
            if mat[x][y] == 'B':
                for p in nbr(x, y):
                    if mat[p[0]][p[1]] != 'G' and mat[p[0]][p[1]] != 'B':
                        mat[p[0]][p[1]] = '#'
    zaj = {}
    for x in range(r):
        for y in range(c):
            zaj[(x, y)] = 0
    if mat[r - 1][c - 1] == '#':
        su = 0
        for i in range(r):
            su += mat[i].count('G')
        if su == 0:
            print("Yes")
        else:
            print("No")
    else:
        zaj[(r - 1, c - 1)] = 1

        def dupa(v):
            q = [v]
            while q:
                w = q.pop(0)
                for u in nbr(w[0], w[1]):
                    if mat[u[0]][u[1]] != '#':
                        if zaj[tuple(u)] == 0:
                            q.append(tuple(u))
                            zaj[tuple(u)] = 1
        dupa((r - 1, c - 1))
        # print(zaj)
        dasie = True
        for x in range(r):
            for y in range(c):
                if mat[x][y] == 'B' and zaj[(x, y)] == 1:
                    dasie = False
                if mat[x][y] == 'G' and zaj[(x, y)] == 0:
                    dasie = False
        if dasie:
            print("Yes")
        else:
            print("No")
