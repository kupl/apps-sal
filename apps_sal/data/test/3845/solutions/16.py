import sys
readline = sys.stdin.readline

A, B = list(map(int, readline().split()))

grid = []
for i in range(50):
    grid.append(["#"] * 100)

for i in range(50):
    grid.append(["."] * 100)

# 前半の黒い部分からA-1箇所を白く塗る
cnt = 0
for i in range(50):
    if cnt >= A - 1:
        break
    for j in range((i % 2) * 2, len(grid[i]), 4):
        if cnt >= A - 1:
            break
        grid[i][j] = "."
        cnt += 1

cnt = 0
for i in range(51, 100):
    if cnt >= B - 1:
        break
    for j in range((i % 2) * 2, len(grid[i]), 4):
        if cnt >= B - 1:
            break
        grid[i][j] = "#"
        cnt += 1

print((100, 100))
for g in grid:
    print(("".join(g)))
