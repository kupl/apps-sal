inp = input()
n, m = inp.split()
n = int(n)
m = int(m)
grid = []
top = n
btm = 0
lft = m
rht = 0
allBlackCount = 0

for i in range(0, n):
    inp = input()
    grid.append(inp)

for i in range(0, n):
    for j in range(0, m):
        if grid[i][j] == 'B':
            top = min(top, i)
            btm = max(btm, i)
            lft = min(lft, j)
            rht = max(rht, j)
            allBlackCount += 1

# print(top,lft)
# print(btm,rht)

h = btm - top + 1
w = rht - lft + 1
sz = max(h, w)

if allBlackCount == 0:
    print(1)
elif sz > n or sz > m:
    print(-1)
else:
    print(sz * sz - allBlackCount)
