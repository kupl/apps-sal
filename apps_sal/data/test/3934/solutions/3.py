import collections
def add_on_tree():
    n = int(input())
    edges = []
    for i in range(n-1): edges.append([int(x) for x in input().split()])
    graph = collections.defaultdict(set)
    for u, v in edges:
        graph[u].add(v)
        graph[v].add(u)
    ans = 'YES'
    for node in graph:
        if len(graph[node]) == 2:
            ans = 'NO'
            break
    print(ans)

add_on_tree()
return
