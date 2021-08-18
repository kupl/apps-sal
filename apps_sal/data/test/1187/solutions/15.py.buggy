'''
  Author: Ashraful Islam Fuad
  University of Asia Pacific
  Bsc in CSE
  category:DFS (dificulty 2000)
  problem :from codeforces 
sd
'''
from collections import defaultdict

ans = defaultdict(lambda: 1)

flag = 0


def dfs(node):
    nonlocal flag
    visit[node] = 1

    for j in graph[node]:
        if not visit[j]:
            dfs(j)

        else:
            if visit[j] == 1:
                flag = 1
                ans[(node, j)] = 2

    visit[node] = 2


n, m = map(int, input().split())

graph = defaultdict(list)


parent = [0] + [i + 1 for i in range(n)]


for i in range(m):
    e1, e2 = map(int, input().split())
    graph[e1].append(e2)

    ans[(e1, e2)] = 1


visit = [0] * (n + 1)


for i in range(n):

    if visit[i] == 0:
        dfs(i)


if flag:
    print(2)
else:
    print(1)

for i in ans:
    # print('i is {}'.format(i))
    print(ans[i], end=' ')
