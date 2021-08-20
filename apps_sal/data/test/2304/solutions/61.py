from collections import deque
import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
inf = pow(10, 10)
(n, m) = list(map(int, input().split()))
a = [inf] * n
edge = [[] for i in range(n)]
for i in range(m):
    (l, r, d) = list(map(int, input().split()))
    l -= 1
    r -= 1
    edge[l].append((r, d))
    edge[r].append((l, -d))
"\n# BFS解放\nflag = True\ndist = [inf] * n\nfor i in range(n):\n    if not flag: break\n    if dist[i] == inf: # 偽の場合、連結で既に訪れている\n        dist[i] = 0\n        dq = deque([i])\n        while dq:\n            now = dq.popleft()\n            for e in edge[now]:\n                nnode, d = e\n                if dist[nnode] == inf:\n                    dist[nnode] = dist[now] + d\n                    dq.append(nnode)\n                else:\n                    if dist[nnode] != dist[now] + d:\n                        flag = False\n                        break\nif flag:\n    print('Yes')\nelse:\n    print('No')\n"
dist = [inf] * n


def dfs(i, totald=0):
    if dist[i] < inf:
        if dist[i] == totald:
            return True
        else:
            return False
    dist[i] = totald
    for e in edge[i]:
        (nnode, d) = e
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
