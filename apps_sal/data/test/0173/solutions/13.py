def dfs(x, y):
    if not graph[2][x + graph[0][x][y]][y]:
        graph[2][x + graph[0][x][y]][y] = True
        dfs(x + graph[0][x][y], y)
    if not graph[2][x][y + graph[1][x][y]]:
        graph[2][x][y + graph[1][x][y]] = True
        dfs(x, y + graph[1][x][y])


n, m = list(map(int, input().split()))
c = chr(0)
flag1 = True
graph = [[[0] * (n + 1) for i in range(m + 1)], [[0] * (n + 1) for i in range(m + 1)], [[False] * (n + 1) for i in range(m + 1)]]

s = input()
for i in range(n):
    c = s[i]
    if c == '<':
        for j in range(1, m):
            graph[0][j][i] = -1
    else:
        for j in range(m - 1):
            graph[0][j][i] = 1

s = input()
for i in range(m):
    c = s[i]
    if c == '^':
        for j in range(1, n):
            graph[1][i][j] = -1
    else:
        for j in range(n - 1):
            graph[1][i][j] = 1

for i in range(n):
    for j in range(m):
        flag = False
        if flag1:
            for k in range(n):
                for l in range(m):
                    graph[2][l][k] = False
            graph[2][j][i] = True
            dfs(j, i)
            for k in range(n):
                for l in range(m):
                    if graph[2][l][k] == False:
                        flag = True
             #           print(i, j, k, l)
            if flag:
                print('NO')
                flag1 = not flag

if flag1:
    print('YES')

# print()
# for i in range(n):
    # for j in range(m):
    #print(graph[0][j][i], end = ' ')
    # print()
# print()
# for i in range(n):
    # for j in range(m):
    #print(graph[1][j][i], end = ' ')
    # print()
