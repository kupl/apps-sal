from collections import defaultdict

n, x, y = list(map(int, input().split()))
sub_checks = [False] * (n + 1)
sub_count = [1] * (n + 1)


def dfs(y, x, graph):
    visited = set()
    s = [y]
    stack_order = []
    while len(s) != 0:
        curr = s.pop()
        visited.add(curr)
        if curr == x:
            sub_checks[curr] = True
        order = []
        for child in graph[curr]:
            if child not in visited:
                s.append(child)
                order.append(child)
        if len(order) != 0:
            stack_order.append((curr, order))

    while len(stack_order) != 0:
        curr = stack_order.pop()
        for child in curr[1]:
            sub_count[curr[0]] += sub_count[child]
            sub_checks[curr[0]] |= sub_checks[child]


graph = defaultdict(list)
for _ in range(n - 1):
    edge = list(map(int, input().split()))
    graph[edge[0]].append(edge[1])
    graph[edge[1]].append(edge[0])

dfs(y, x, graph)

exclude = 0
for child in graph[y]:
    if sub_checks[child]:
        exclude = sub_count[y] - sub_count[child]
        break

print(n * (n - 1) - (exclude * sub_count[x]))
