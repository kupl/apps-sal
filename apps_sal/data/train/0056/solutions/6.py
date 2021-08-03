t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = k // n
    rem = k % n
    grid = []
    for i in range(n):
        grid.append([])
        for j in range(n):
            grid[-1].append('0')
    for i in range(n):
        for j in range(i, i + a):
            grid[i][j % n] = '1'
        if i < rem:
            grid[i][(i + a) % n] = '1'
    ans = 0
    r = []
    for i in range(n):
        p = 0
        for j in range(n):
            if grid[i][j] == '1':
                p += 1
        r.append(p)
    c = []
    for i in range(n):
        p = 0
        for j in range(n):
            if grid[j][i] == '1':
                p += 1
        c.append(p)
    print((max(r) - min(r))**2 + (max(c) - min(c))**2)
    for i in range(n):
        ans = ''.join(grid[i])
        print(ans)
