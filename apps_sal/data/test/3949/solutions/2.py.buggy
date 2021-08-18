n, m = [int(x) for x in input().split()]

grid = [input() for _ in range(n)]

imp_flag = False
empty_row_flag = False
empty_col_flag = False

for row in grid:
    flag = False
    for i in range(m - 1):
        if not flag and row[i] == "#" and row[i + 1] == ".":
            flag = True
        elif flag and row[i] == "." and row[i + 1] == "#":
            imp_flag = True
            break
    if all(x == "." for x in row):
        empty_row_flag = True
    if imp_flag:
        break

for col_i in range(m):
    flag = False
    for i in range(n - 1):
        if not flag and grid[i][col_i] == "#" and grid[i + 1][col_i] == ".":
            flag = True
        elif flag and grid[i][col_i] == "." and grid[i + 1][col_i] == "#":
            imp_flag = True
            break
    if all(grid[j][col_i] == "." for j in range(n)):
        empty_col_flag = True
    if imp_flag:
        break

if imp_flag or (empty_row_flag != empty_col_flag):
    import sys
    print(-1)
    return

cc = 0
cs = [[-1] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if grid[i][j] == "." or cs[i][j] != -1:
            continue
        cs[i][j] = 1
        cc += 1

        s = [(i, j)]
        while len(s):
            ci, cj = s.pop()
            for nbi, nbj in [(ci - 1, cj), (ci + 1, cj), (ci, cj + 1), (ci, cj - 1)]:
                if 0 <= nbi < n and 0 <= nbj < m and cs[nbi][nbj] == -1 and \
                        grid[nbi][nbj] == "#":
                    cs[nbi][nbj] = cs[ci][cj]
                    s.append((nbi, nbj))

print(cc)
