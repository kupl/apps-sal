(n, m) = [int(x) for x in input().split()]
graph = {}
for i in range(m):
    (a, b) = [int(x) for x in input().split()]
    for (a, b) in ((a, b), (b, a)):
        if a not in graph:
            graph[a] = [b]
        else:
            graph[a].append(b)


def tree(new):
    total = []
    for v in new:
        for item in graph[v]:
            if item not in invite:
                total.append((v, item))
                invite.add(item)
                new.append(item)
    return total


index = max_rou = 0
for v in graph:
    if len(graph[v]) > max_rou:
        max_rou = len(graph[v])
        index = v
invite = set([index])
answer = tree([index])
for i in range(n - 1):
    print(*answer[i])
