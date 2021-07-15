import sys

input = sys.stdin.readline
H, W = map(int, input().split())
grid = []
for _ in range(H):
    grid.append(list(input().strip()))

h_set = set()
for i in range(H):
    flag = True
    for j in range(W):
        if grid[i][j] == "#":
            flag = False
            break
    if flag:
        h_set.add(i)

w_set = set()
for j in range(W):
    flag = True
    for i in range(H):
        if grid[i][j] == "#":
            flag = False
            break
    if flag:
        w_set.add(j)

for i in range(H):
    if i in h_set:
        continue
    for j in range(W):
        if j in w_set:
            continue
        print(grid[i][j], end="")
    print("")
