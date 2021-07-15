# -*- coding: utf-8 -*-
n, m = map(int, input().split(' '))
edges = [[] for i in range(n + 1)]
vis = [False] * (n + 1)

def dfs(a):
    nonlocal cnt_vertices
    nonlocal cnt_edges
    stack = [a]
    while len(stack) > 0:
        a = stack.pop()
        if vis[a]:
            continue
        vis[a] = True
        cnt_vertices += 1
        cnt_edges += len(edges[a])
        for b in edges[a]:
            if not vis[b]:
                stack.append(b)

while m > 0:
    a, b = map(int, input().split(' '))
    edges[a].append(b)
    edges[b].append(a)
    m -= 1
for i in range(1, n+1):
    if vis[i] == False:
        cnt_vertices = 0
        cnt_edges = 0
        dfs(i)
        if cnt_edges != cnt_vertices*(cnt_vertices-1):
            print("NO")
            return
print("YES")
