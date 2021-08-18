
from collections import defaultdict
ans = defaultdict(lambda: 1)
flag = 0


def dfs(i):

    nonlocal flag
    vis[i] = 1

    for j in hash[i]:
        if not vis[j]:
            dfs(j)
        else:
            if vis[j] == 1:
                flag = 1

                ans[(i, j)] = 2

    vis[i] = 2


n, m = map(int, input().split())

hash = defaultdict(list)

par = [0] + [i + 1 for i in range(n)]


for i in range(m):
    a, b = map(int, input().split())

    hash[a].append(b)

    ans[(a, b)] = 1

vis = [0] * (n + 1)

for i in range(n):
    if vis[i] == 0:
        dfs(i)
if flag:
    print(2)
else:
    print(1)
for i in ans:
    print(ans[i], end=' ')
