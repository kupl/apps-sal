def __starting_point():
    n = int(input())
    edges = [[] for i in range(n + 1)]
    edges[0] = None
    for i in range(n - 1):
        (n1, n2) = list(map(int, input().split()))
        edges[n1].append(n2)
        edges[n2].append(n1)
    stack = [(1, 0, 1.0)]
    sev = 0
    visited = [False for i in range(n + 1)]
    while len(stack) > 0:
        (node, height, prob) = stack.pop()
        visited[node] = True
        children = len(edges[node]) - 1
        if node == 1:
            children += 1
        for child in edges[node]:
            if visited[child]:
                continue
            stack.append((child, height + 1, prob / children))
        if children == 0:
            sev += height * prob
    print(sev)


__starting_point()
