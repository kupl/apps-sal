# A
'''
n, m = map(int, input().split())
row = ['#' * m if i % 2 == 0 else '.' * (m - 1) + '#' if i % 4 == 1
       else '#' + '.' * (m - 1) for i in range(n)]
print('\n'.join(row))
'''
# B
import sys
sys.setrecursionlimit(5000)
n, m = list(map(int, input().split()))
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]
L = list(input() for i in range(n))


def check(x, y, px, py):
    return (x >= 0 and x < n and y >= 0 and y < m)


def DFS(x, y, px, py, visited):
    #print(x, y, px, py, '\n', visited)
    visited[x][y] = True
    for i in range(4):
        newx = x + dx[i]
        newy = y + dy[i]
        if not check(newx, newy, px, py):
            continue
        if (newx == px and newy == py):
            continue
        #print('Bug ', visited)
        if L[x][y] == L[newx][newy]:
            if visited[newx][newy]:
                #print('Here True', newx, newy, x, y)
                return True
            if DFS(newx, newy, x, y, visited):
                #print(newx, newy, x, y, visited)
                return True
    return False


def solve():
    #    visited = [[False] * m] * n
    visited = [[False for j in range(m)] for i in range(n)]
    for i in range(n):
        for j in range(m):
            if visited[i][j]:
                continue
            if DFS(i, j, -1, -1, visited):
                return True
    return False


print('Yes' if solve() else 'No')
'''
3 3
AAA
ABA
ABA
'''
