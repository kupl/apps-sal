from collections import deque
import sys
DBG = False
n, m, p = list(map(int, input().split()))
spd = list(map(int, input().split()))
spd.insert(0, -1)  # p starts at 1
grid = [[0] * m for i in range(n)]
c2d = {"#": -1, ".": 0, "1": 1, "2": 2, "3": 3, "4": 4,
       "5": 5, "6": 6, "7": 7, "8": 8, "9": 9}
castle = [[] for i in range(p + 1)]

for i in range(n):
    s = input()
    for j in range(m):
        v = c2d[s[j]]
        grid[i][j] = v
        if v > 0:
            castle[v].append([i, j])

if DBG:
    print(grid)
    print("\n")
    print(spd)
    print("\n")


def mark(proc, t):
    nonlocal changed, grid, castle, newcastle
    dir = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    while len(proc) > 0:
        ent = proc.popleft()
        c = ent[0]
        s = ent[1]
        for d in dir:
            x = c[0] + d[0]
            y = c[1] + d[1]
            if x < 0 or n <= x or y < 0 or m <= y or grid[x][y] != 0:
                continue
            changed = True
            grid[x][y] = t
            if s > 1:
                proc.append([[x, y], s - 1])
            else:
                newcastle.append([x, y])


changed = True
while changed:
    if DBG:
        print("---- new loop ----")
    changed = False
    for t in range(1, p + 1):
        newcastle = []
        proc = deque([])
        for c in castle[t]:
            proc.append([c, spd[t]])
        mark(proc, t)
        if False and DBG:
            print(("turn for %d, (%d,%d) ended" %
                   (t, c[0], c[1])))
            print(grid)
        # for x in $newcastle
        #  $castle[t] << x
        # end
        castle[t] = newcastle

a = [0 for i in range(p + 1)]
for x in range(n):
    for y in range(m):
        if grid[x][y] != -1:
            a[grid[x][y]] += 1

for i in range(1, p + 1):
    sys.stdout.write("%d " % a[i])
print("")
