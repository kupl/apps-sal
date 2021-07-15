import sys

def get_array(): return list(map(int, sys.stdin.readline().split()))
def get_ints(): return list(map(int, sys.stdin.readline().split()))
def input(): return sys.stdin.readline().strip('\n')

cells = []

''' Using pajenegod dfs '''
def dfs(x,y):
    nonlocal c
    q = [(x,y)]

    while q:
        x, y = q.pop()
        if x >= n or x < 0 or y >= m or y < 0:
            continue
        if l[x][y] == '*':
            c += 1
            continue
        if visited[x][y]:
            continue
        
        visited[x][y] = 1
        cells.append((x,y))
        q.append((x+1,y))
        q.append((x,y+1))
        q.append((x-1,y))
        q.append((x,y-1))

n , m , k = get_ints()
l = []
for i in range(n):
    l.append(list(input()))

visited = []
out = []

for i in range(n+10):
    visited.append([0]*(m+10))
    out.append([-1]*(m+10))
    
for i in range(n):
    for j in range(m):
        if not visited[i][j] and l[i][j] == '.':
            c = 0
            dfs(i,j)
            for x in cells:
                if visited[x[0]][x[1]] and out[x[0]][x[1]] == -1:
                    out[x[0]][x[1]] = c
            cells.clear()
for i in range(k):
    x , y = get_ints()
    x , y = x-1 , y-1
    print(out[x][y])

