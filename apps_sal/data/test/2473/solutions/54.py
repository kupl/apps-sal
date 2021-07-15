import sys
stdin = sys.stdin
ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
nn = lambda: list(stdin.readline().split())
ns = lambda: stdin.readline().rstrip()
sys.setrecursionlimit(10**6)

n,k = na()
xy = []

for i in range(n):
    x,y = na()
    xy.append((x,y))

xy.sort()
ans = 10000000000000000000000000000

for i in range(n):
    for j in range(i+1, n):
        x = xy[j][0] - xy[i][0]
        yy = sorted(xy[i:j+1], key=lambda x:x[1])
        for u in range(len(yy)-k+1):
            y = yy[u+k-1][1] - yy[u][1]
            ans = min(ans, y*x)
            
print(ans)

