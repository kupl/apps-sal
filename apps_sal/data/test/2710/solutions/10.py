# coding:utf-8
"""
 CF546E 
"""
import sys
import copy
import os

# sys.stdin = open(os.path.join(os.path.dirname(__file__), 'in1'))

n, m = map(lambda x: int(x), input().strip().split())
a = [_ for _ in map(lambda x:int(x), input().strip().split())]
b = [_ for _ in map(lambda x:int(x), input().strip().split())]
INF = 2 << 40
G = [[0 for _ in range(2 * n + 2)] for i in range(2 * n + 2)]
F = [[0 for _ in range(2 * n + 2)] for i in range(2 * n + 2)]

for i in range(1, n + 1):
    G[0][i] = a[i - 1]
    G[i][i + n] = INF
    G[i + n][2 * n + 1] = b[i - 1]

for i in range(m):
    p, q = map(lambda x: int(x), input().strip().split())
    # add
    G[p][q + n] = INF
    G[q][p + n] = INF


Vs = [False for i in range(2 * n + 2)]

total = 0


def dfs(st, t, v):
    nonlocal find, V, minv, total, G
    V[st] = True
    i = 0
    while i <= 2 * n + 1:
        if G[st][i] > 0 and not V[i]:
            # print(i)
            if i == t:
                V[i] = True
                find = True
                minv = min([v, G[st][i]])
                G[st][i] = G[st][i] - minv
                G[i][st] = G[i][st] + minv
                F[st][i] += minv
                if F[i][st] > 0:
                    F[i][st] -= minv
                total += minv
                return minv
            mv = dfs(i, t, min([v, G[st][i]]))
            if mv > 0:
                F[st][i] += minv
                if F[i][st] > 0:
                    F[i][st] -= minv
                G[st][i] = G[st][i] - minv
                G[i][st] = G[i][st] + minv
                return mv
        i += 1
    return 0


while True:
    find = False
    V = copy.deepcopy(Vs)
    minv = (2 << 40)
    mv = dfs(0, 2 * n + 1, minv)
    if not find:
        break
if total == sum(a) and total == sum(b):
    print("YES")
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == j:
                print(F[i][i + n], end=' ')
            else:
                print(F[i][j + n], end=' ')
        print()
else:
    print("NO")
