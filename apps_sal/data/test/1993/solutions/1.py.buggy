# n=int(input())
# n,k=map(int,input().split())
# arr=list(map(int,input().split()))
# ls=list(map(int,input().split()))
# for i in range(m):
# for _ in range(int(input())):
from collections import Counter
#from fractions import Fraction
# n=int(input())
# arr=list(map(int,input().split()))
#ls = [list(map(int, input().split())) for i in range(n)]
from math import log2
# for _ in range(int(input())):
#n, m = map(int, input().split())
# for _ in range(int(input())):
from math import gcd
# n=int(input())
# for i in range(m):
# for i in range(int(input())):
# n,k= map(int, input().split())
# arr=list(map(int,input().split()))
# n=sys.stdin.readline()
# n=int(n)
# n,k= map(int, input().split())
# arr=list(map(int,input().split()))
# n=int(inaput())
# for _ in range(int(input())):
# arr=list(map(int,input().split()))
from collections import deque
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]


def bfs(x, y):
    nonlocal total
    total += 1
    q = deque([(x, y)])
    v[x][y] = True
    h[x][y] = comp
    # q.append()
    while q:
        x, y = q.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            #print("nx,y",nx, ny)
            if (nx >= 0 and nx < n) and (ny >= 0 and ny < m) and (v[nx][ny] == False) and (g[nx][ny] == "."):
                q.appendleft((nx, ny))
                total += 1
                v[nx][ny] = True
                h[nx][ny] = comp


# nonlocal g,h,r,comp,total
n, m = list(map(int, input().split()))
h = [[-1 for i in range(m)] for j in range(n)]
g = []
v = [[False for i in range(m)]for j in range(n)]
for i in range(n):
    g.append(list(input()))
component = []
for i in range(n):
    for j in range(m):
        if v[i][j] == False and g[i][j] == ".":
            comp = len(component)
            # nonlocal total
            total = 0
            bfs(i, j)
            component.append(total)
# print(component)
for x in range(n):
    for y in range(m):
        if g[x][y] == "*":
            ans = 0
            s = set()
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                if nx >= 0 and nx < n and ny >= 0 and ny < m and g[nx][ny] == ".":
                    s.add(h[nx][ny])
            for itm in s:
                ans += component[itm]
            ans += 1
            ans %= 10
            g[x][y] = str(ans)
for i in range(n):
    print("".join(g[i]))
