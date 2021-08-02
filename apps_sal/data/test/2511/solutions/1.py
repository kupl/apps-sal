import sys
from collections import deque
def input(): return sys.stdin.readline().rstrip()


def per(n, r, mod=10**9 + 7):  # 順列数
    per = 1
    for i in range(r):
        per = per * (n - i) % mod
    return per


n, k = map(int, input().split())
mod = 10**9 + 7
graph = [[] for _ in range(n + 1)]

for i in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dist = [-1] * (n + 1)
dist[0] = 0
dist[1] = 0

d = deque()
d.append(1)
ans = k
while d:
    v = d.popleft()
    cnt = 0
    for i in graph[v]:
        if dist[i] != -1:
            continue
        dist[i] = dist[v] + 1
        d.append(i)
        cnt += 1
    if cnt > 0:
        if v == 1:
            ans = ans * per(k - 1, cnt) % mod
        else:
            ans = ans * per(k - 2, cnt) % mod


print(ans)
