import sys
input = sys.stdin.readline


def topological_sort(graph) -> list:
    n = len(graph)
    degree = [0] * n
    for g in graph:
        for next_pos in g:
            degree[next_pos] += 1
    
    ans = [i for i in range(n) if degree[i] == 0]

    stack = ans[:]
    while stack:
        pos = stack.pop()
        for next_pos in graph[pos]:
            degree[next_pos] -= 1
            if degree[next_pos] == 0:
                stack.append(next_pos)
                ans.append(next_pos)
    return ans



n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

graph = [[] for i in range(n)]
inv_graph = [[] for i in range(n)]
for v, nxt_v in enumerate(b):
    if nxt_v == -1:
        continue
    nxt_v -= 1
    graph[v].append(nxt_v)
    inv_graph[nxt_v].append(v)

ans = 0
res = []
used = [False] * n

tp_sorted = topological_sort(graph)
for v in tp_sorted:
    if used[v]:
        continue
    if a[v] >= 0:
        ans += a[v]
        for nxt_v in graph[v]:
            a[nxt_v] += a[v]
        used[v] = True
        res.append(v + 1)

tp_sorted = topological_sort(inv_graph)
for v in tp_sorted:
    if used[v]:
        continue
    ans += a[v]
    used[v] = True
    res.append(v + 1)

print(ans)
print(*res)
