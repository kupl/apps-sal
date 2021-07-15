import sys
sys.setrecursionlimit(3000)

n,m = map(int, input().split(' '))
L = []
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]
for i in range(n) :
    L.append(input())

def dfs(y, x, p_y, p_x, visited) :
    nonlocal dx, dy, n, m, L
    visited[y][x] = 1
    for i in range(4) :
        new_y = y + dy[i]
        new_x = x + dx[i]
        if new_y < 0 or new_y >= n or new_x < 0 or new_x >= m : continue
        if new_y == p_y and new_x == p_x : continue
        if L[y][x] == L[new_y][new_x] :
            if visited[new_y][new_x] == 1: return True
            if dfs(new_y, new_x, y, x, visited) : return True
    return False

def solve() :
    nonlocal n,m,L
    visited = [[0 for j in range(m)] for i in range(n)]
    for i in range(n) :
        for j in range(m) :
            if visited[i][j] == 1:continue
            if dfs(i, j, -1, -1, visited) :
                return True
    return False

if solve() : print("Yes")
else : print("No")
