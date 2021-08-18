import itertools
N, M = map(int, input().split())
edges = [list(map(int, input().split())) for i in range(M)]
graph = [[] for i in range(N + 1)]
for edge in edges:
    graph[edge[0]].append(edge[1])
    graph[edge[1]].append(edge[0])

node = [i for i in range(1, N + 1)]
per_list = list(itertools.permutations(node))
count = 0
for l in per_list:
    if l[0] != 1:
        continue
    flg = 0
    for i in range(len(l) - 1):
        if not (l[i + 1] in graph[l[i]]):
            flg = 1
            break
    if not flg:
        count += 1

print(count)
