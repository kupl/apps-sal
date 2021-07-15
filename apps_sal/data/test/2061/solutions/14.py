import sys

sys.setrecursionlimit(5000)

n, m, k = [int(x) for x in input().split()]

land = []
cc = 0
visit = [[0 for _ in range(m)] for _ in range(n)]
for i in range(n):
    land.append(list(input()))
edge = False

def DFS(i, j, c):
    nonlocal land, n, m, k, cc, visit, edge
    if i <= 0 or j <= 0 or i >= n-1 or j >= m-1:
        edge = True
        return 0
    if visit[i][j] != 0: return 0
    if land[i][j] == '*': return 0
    visit[i][j] = 1
    cc += 1
    if land[i + 1][j] == '.': DFS(i + 1, j, c + 1)
    if land[i - 1][j] == '.': DFS(i - 1, j, c + 1)
    if land[i][j + 1] == '.': DFS(i, j + 1, c + 1)
    if land[i][j - 1] == '.': DFS(i, j - 1, c + 1)

def DFS2(i, j):
    nonlocal land, n, m, k, cc
    if i < 0 or j < 0 or i >= n or j >= m: return 0
    if land[i][j] != '.': return 0
    land[i][j] = '*'
    DFS2(i+1,j)
    DFS2(i - 1, j)
    DFS2(i, j+1)
    DFS2(i, j-1)
    return 0


ccc = []
pos = []

for i in range(n):
    for j in range(m):
        cc = 0
        edge = False
        if visit[i][j] == 0:
            DFS(i,j,0)
            if edge is True: continue
            if cc > 0:
                ccc.append([cc, i, j])


ccc.sort()

red =len(ccc) - k

if red == 0:
    print(0)
    for i in range(n):
        print(''.join(land[i]))
    return

red_list = ccc[0:red]

p = [x[0] for x in red_list]
print(sum(p))

for i in range(len(red_list)):
    DFS2(red_list[i][1], red_list[i][2])

for i in range(n):
    print(''.join(land[i]))
