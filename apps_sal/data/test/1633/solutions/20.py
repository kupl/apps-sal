x = input()
(n, m, k) = x.split(maxsplit=100)
(n, m, k) = (int(n), int(m), int(k))
mapp = [[0 for j in range(m)] for i in range(n)]
maqq = [[0 for j in range(m - 1)] for i in range(n - 1)]
u = [(0, 0), (0, -1), (-1, 0), (-1, -1)]
key = False
for i in range(k):
    x = input()
    if key:
        continue
    (x, y) = x.split(maxsplit=100)
    (x, y) = (int(x) - 1, int(y) - 1)
    if mapp[x][y] == 1:
        continue
    else:
        mapp[x][y] += 1
        for j in range(4):
            try:
                assert x + u[j][0] >= 0 and y + u[j][1] >= 0
                maqq[x + u[j][0]][y + u[j][1]] += 1
                if maqq[x + u[j][0]][y + u[j][1]] == 4:
                    print(i + 1)
                    key = 1
                    break
            except Exception:
                pass
if not key:
    print(0)
