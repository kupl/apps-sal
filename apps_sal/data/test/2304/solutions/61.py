from collections import deque
import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline
inf = pow(10, 10)

n, m = list(map(int, input().split()))
a = [inf] * n

edge = [[] for i in range(n)]

for i in range(m):
    l, r, d = list(map(int, input().split()))
    l -= 1
    r -= 1
    edge[l].append((r, d))
    edge[r].append((l, -d))

"""
# BFS解放
flag = True
dist = [inf] * n
for i in range(n):
    if not flag: break
    if dist[i] == inf: # 偽の場合、連結で既に訪れている
        dist[i] = 0
        dq = deque([i])
        while dq:
            now = dq.popleft()
            for e in edge[now]:
                nnode, d = e
                if dist[nnode] == inf:
                    dist[nnode] = dist[now] + d
                    dq.append(nnode)
                else:
                    if dist[nnode] != dist[now] + d:
                        flag = False
                        break
if flag:
    print('Yes')
else:
    print('No')
"""

# DFS解法
dist = [inf] * n


def dfs(i, totald=0):
    if dist[i] < inf:
        if dist[i] == totald:
            return True
        else:
            return False
    dist[i] = totald
    for e in edge[i]:
        nnode, d = e
        if not dfs(nnode, totald + d):
            return False
    return True


f = True
for i in range(n):
    if dist[i] == inf:
        if not dfs(i, 0):
            f = False
            break
if f:
    print('Yes')
else:
    print('No')
