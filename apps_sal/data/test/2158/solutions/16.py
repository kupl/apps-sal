n = int(input())
al = [[] for j in range(n)]
for i in range(n - 1):
    (a, b, c) = list(map(int, input().split()))
    al[a].append([b, c])
    al[b].append([a, c])
mc = 0
va = [0] * n
ca = [0] * n


def dfs(n, c):
    va[n] = 1
    ca[n] = ca[n] + c
    for e in al[n]:
        p = e[0]
        q = e[1] + ca[n]
        if va[p] == 0:
            dfs(p, q)


dfs(0, 0)
print(max(ca))
'\nmc = 0\ncost = 0\nvisited = [False] * n\ndef DFS(num,visited,cost):\n    nonlocal mc\n    if cost > mc:\n        mc = cost\n    visited[num] = True\n    for i in range(len(li[num])):\n        if not visited[li[num][i][0]]:\n            DFS(li[num][i][0],visited,cost+li[num][i][1])\nDFS(0,visited,0)\nprint(mc)'
