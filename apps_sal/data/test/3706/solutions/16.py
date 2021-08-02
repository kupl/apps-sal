n, m = map(int, input().split())
grid = [list(map(int, input().split())) for i in range(n)]
ans = []
if m > n:
    for i in range(n):
        mini = min(grid[i])
        for j in range(m):
            grid[i][j] -= mini
        for _ in range(mini):
            ans.append("row " + str(i + 1))
    for i in range(m):
        mini = float('inf')
        for j in range(n):
            mini = min(grid[j][i], mini)
        for j in range(n):
            grid[j][i] -= mini
        for _ in range(mini):
            ans.append("col " + str(i + 1))
else:
    for i in range(m):
        mini = float('inf')
        for j in range(n):
            mini = min(grid[j][i], mini)
        for j in range(n):
            grid[j][i] -= mini
        for _ in range(mini):
            ans.append("col " + str(i + 1))
    for i in range(n):
        mini = min(grid[i])
        for j in range(m):
            grid[i][j] -= mini
        for _ in range(mini):
            ans.append("row " + str(i + 1))
if all([sum(i) == 0 for i in grid]):
    print(len(ans))
    for i in ans:
        print(i)
else:
    print(-1)
