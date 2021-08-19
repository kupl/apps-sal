import sys
import math
import queue
sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
(n, m, h) = map(int, input().split())
front = list(map(int, input().split()))
side = list(map(int, input().split()))
top = []
for i in range(n):
    top.append(list(map(int, input().split())))
ans = [[-1 for i in range(m)] for j in range(n)]
for i in range(n):
    for j in range(m):
        if top[i][j] == 0:
            ans[i][j] = 0
        else:
            ans[i][j] = min(front[j], side[i])
for row in ans:
    print(*row)
