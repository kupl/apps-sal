import copy
from collections import deque

n, st, sa = map(int,input().split())
st -= 1
sa -= 1

e = [[] for i in range(n)]
for i in range(n-1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    e[a].append(b)
    e[b].append(a)

visited = [False] * n
visited[st] = True
d = deque()
d.append([st, 0])
tx = {}
if len(e[st]) == 1:
    tx[st] = 0
cnt = 0
while d:
    f, cnt = d.popleft()
    flg = True
    for t in e[f]:
        if not visited[t]:
            flg = False
            d.append([t, cnt+1])
            visited[t] = True
    if flg:
        tx[f] = cnt

visited = [False] * n
visited[sa] = True
d = deque()
d.append([sa, 0])
ax = {}
if len(e[sa]) == 1:
    ax[sa] = 0
cnt = 0
while d:
    f, cnt = d.popleft()
    flg = True
    for t in e[f]:
        if not visited[t]:
            flg = False
            d.append([t, cnt+1])
            visited[t] = True
    if flg:
        ax[f] = cnt

ax = sorted(ax.items(), key=lambda x:x[1], reverse=True)
for i in range(len(ax)):
    x, d = ax[i][0], ax[i][1]
    if d > tx[x]:
        ans = d - 1
        break

print(ans)
