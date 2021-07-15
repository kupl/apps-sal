import sys, math
def bfs(a):
    Q = [a]
    ctr = 0
    used = [[0] * m for i in range(n)]
    while ctr < len(Q):
        h = Q[ctr]
        ctr += 1
        z[h[0]][h[1]] = 'o'
        if h[0] - 1 >= 0 and z[h[0] - 1][h[1]] == '.' and not used[h[0] - 1][h[1]]:
            Q.append([h[0] - 1, h[1]])
            used[h[0] - 1][h[1]] = 1
        if h[0] + 1 < n and z[h[0] + 1][h[1]] == '.' and not used[h[0] + 1][h[1]]:
            Q.append([h[0] + 1, h[1]])
            used[h[0] + 1][h[1]] = 1
        if h[1] - 1 >= 0 and z[h[0]][h[1] - 1] == '.' and not used[h[0]][h[1] - 1]:
            Q.append([h[0], h[1] - 1])
            used[h[0]][h[1] - 1] = 1
        if h[1] + 1 < m and z[h[0]][h[1] + 1] == '.' and not used[h[0]][h[1] + 1]:
            Q.append([h[0], h[1] + 1])
            used[h[0]][h[1] + 1] = 1

def bfs1(a, b):
    Q = [a]
    ctr = 0
    while ctr < len(Q):
        h = Q[ctr]
        ctr += 1
        if z[h[0]][h[1]] == b:
            continue
        z[h[0]][h[1]] = b
        if h[0] - 1 >= 0 and z[h[0] - 1][h[1]] == '.':
            Q.append([h[0] - 1, h[1]])
        if h[0] + 1 < n and z[h[0] + 1][h[1]] == '.':
            Q.append([h[0] + 1, h[1]])
        if h[1] - 1 >= 0 and z[h[0]][h[1] - 1] == '.':
            Q.append([h[0], h[1] - 1])
        if h[1] + 1 < m and z[h[0]][h[1] + 1] == '.':
            Q.append([h[0], h[1] + 1])
    ctr = 0
    for i in range(n):
        for j in range(m):
            if z[i][j] == b:
                ctr += 1
    return ctr
        
n, m, k = map(int, input().split())
z = [list(input()) for i in range(n)]
for i in range(n):
    if z[i][0] == '.':
        bfs([i, 0])
    if z[i][m - 1] == '.':
        bfs([i, m - 1])
for i in range(m):
    if z[0][i] == '.':
        bfs([0, i])
    if z[n - 1][i] == '.':
        bfs([n - 1, i])
ctr = 0
z1 = []
for i in range(n):
    for j in range(m):
        if z[i][j] == '.':
            z1.append([bfs1([i, j], ctr), ctr])
            ctr += 1
z1.sort()
dif = ctr - k
ans = 0
for i in range(dif):
    u = z1[i][1]
    ans += z1[i][0]
    for j in range(n):
        for k in range(m):
            if z[j][k] == u:
                z[j][k] = '*'
for i in range(n):
    for j in range(m):
        if z[i][j] != '*' and z[i][j] != '.':
            z[i][j] = '.'
print(ans)
for i in range(n):
    print(*z[i], sep = '')
    
            
            




