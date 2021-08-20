def solve(n, m):
    grid = []
    for i in range(n):
        grid.append(input().strip())
        cnt = 0
        for j in range(1, m):
            if grid[i][j] != grid[i][j - 1]:
                cnt += 1
        if cnt > 2 or (cnt == 2 and grid[i][0] == 'B'):
            return False
    for j in range(m):
        cnt = 0
        for i in range(1, n):
            if grid[i][j] != grid[i - 1][j]:
                cnt += 1
        if cnt > 2 or (cnt == 2 and grid[0][j] == 'B'):
            return False
    bps = []
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 'B':
                bp1 = (i, j)
                for k in range(len(bps)):
                    bp2 = bps[k]
                    if not (grid[bp1[0]][bp2[1]] == 'B' or grid[bp2[0]][bp1[1]] == 'B'):
                        return False
                bps.append((i, j))
    return True


def __starting_point():
    (n, m) = list(map(int, input().strip().split()))
    ans = solve(n, m)
    if ans:
        print('YES')
    else:
        print('NO')


__starting_point()
