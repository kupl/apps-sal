import sys
sys.setrecursionlimit(10**7)


n = int(input())
col = [0] * n
next = [[] for i in range(n)]
d = [float('INF')] * n
d[0] = 0


def dfs(now, parent):
    for next1, w1 in next[now]:
        if next1 == parent:
            continue
        elif d[next1] == float('INF'):
            d[next1] = d[now] + w1
            dfs(next1, now)


for i in range(n - 1):
    u, v, w = list(map(int, input().split()))
    next[u - 1].append((v - 1, w))
    next[v - 1].append((u - 1, w))

dfs(0, -1)

for i in range(n):
    if d[i] % 2 == 0:
        print('0')
    else:
        print('1')
