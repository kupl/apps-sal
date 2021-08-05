from collections import defaultdict
from collections import deque

g = defaultdict(lambda: [])

s = input().strip()
ls = len(s)

vis = [False for i in range(ls)]
dis = [0 for i in range(ls)]

for i in range(1, ls):
    g[s[i]].append(i)


que = deque()

que.append(0)
vis[0] = True

while que:
    indx = que.popleft()

    if indx == ls - 1:
        break

    temp = s[indx]

    for i in g[temp]:
        if not vis[i]:
            vis[i] = True
            que.append(i)
            dis[i] = dis[indx] + 1

    g[temp].clear()

    if indx - 1 >= 0 and not vis[indx - 1]:
        vis[indx - 1] = True
        que.append(indx - 1)
        dis[indx - 1] = dis[indx] + 1

    if indx + 1 < ls and not vis[indx + 1]:
        vis[indx + 1] = True
        que.append(indx + 1)
        dis[indx + 1] = dis[indx] + 1


print(dis[-1])
