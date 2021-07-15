n, m = map(int, input().split())
a = input()
b = input()
f = True
def dfs(x, y):
    tmp = 1
    used[x + y * 42] = 1
    if a[x] == '>' and y + 1 < m:
        if used[x + (y + 1) * 42] == 0:
            tmp += dfs(x, y + 1)
    if a[x] == '<' and y - 1 >= 0:
        if used[x + (y - 1) * 42] == 0:
            tmp += dfs(x, y - 1)
    if b[y] == 'v' and x + 1 < n:
        if used[x + 1 + (y) * 42] == 0:
            tmp += dfs(x + 1, y)
    if b[y] == '^' and x - 1 >= 0:
        if used[x - 1 + (y) * 42] == 0:
            tmp += dfs(x - 1, y)
    return(tmp)
    
for i in range(n):
    for j in range(m):
        used = [0] * 1000
        if dfs(i, j) != n * m:
            f = False
if f:
    print('YES')
else:
    print('NO')
