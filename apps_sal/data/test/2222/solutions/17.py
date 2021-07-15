n = int(input())
oper = list(map(int, input().split())) # 0 - min, 1 - max
prev = [int(i) - 1 for i in input().split()]

graph = [[] for i in range(n)]
for i in range(n - 1):
    graph[prev[i]].append(i + 1) 

leafs = sum([len(graph[i]) == 0 for i in range(n)])

res = [0] * n
for u in range(n - 1, -1, -1):
    if len(graph[u]) == 0:
        res[u] = 1
    else:
        sons = [res[v] for v in graph[u]]
        res[u] = (min(sons) if oper[u] == 1 else sum(sons))
print(leafs - res[0] + 1)
