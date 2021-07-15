n, m = list(map(int, input().split()))
vs = list(map(int, input().split()))
if m == 0:
    print(sum(vs))
    return
# n = 100000
# m = n - 1
# vs = [0] * n
es = {i: [] for i in range(n)}
visited = {i: False for i in range(n)}
comps = []


# def dfs(vv, compp):
#     # nonlocal visited, es
#     if visited[vv]:
#         return
#     visited[vv] = True
#     compp.append(vv)
#     neighs = es[vv]
#     for neigh in neighs:
#         if visited[neigh] or neigh == vv:
#             continue
#         dfs(neigh, compp)


for i in range(m):
    f, t = list(map(int, input().split()))
    # f, t = i + 1, i + 2
    es[f-1].append(t-1)
    es[t-1].append(f-1)

for v in range(n):
    if visited[v]:
        continue
    comp = []
    deque = [v]
    while deque:
        v_temp = deque.pop(0)
        if visited[v_temp]:
            continue
        visited[v_temp] = True
        comp.append(v_temp)
        for neigh in es[v_temp]:
            if visited[neigh] or neigh == v_temp:
                continue
            deque.append(neigh)
    comps.append(comp)
# print(es)
res = 0
for comp in comps:
    if not comp:
        continue
    res += min(vs[i] for i in comp)

print(res)

