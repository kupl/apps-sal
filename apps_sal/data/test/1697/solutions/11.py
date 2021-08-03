import sys
#sys.stdin = open('in.txt')
sys.setrecursionlimit(10000)
def isin(x, y): return 0 <= x < n and 0 <= y < m


def dfs(curx, cury, fax=-1, fay=-1):
    nonlocal found
    vis[curx][cury] = True
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    for i in range(4):
        newx = curx + dx[i]
        newy = cury + dy[i]
        if isin(newx, newy):
            if G[curx][cury] == G[newx][newy] and vis[newx][newy] and not (newx
 ==
                                                                           fax and newy == fay):
                found = True
                print("Yes")
                return
            if G[curx][cury] == G[newx][newy] and not vis[newx][newy]:
                dfs(newx, newy, curx, cury)


n, m = map(int, input().split())
vis = [[False] * m for _ in range(n)]
G = [input() for _ in range(n)]
found = False
for i in range(n):
    for j in range(m):
        if not vis[i][j]:
            dfs(i, j)
        if found:
            print('Yes')
            return
print('No')
