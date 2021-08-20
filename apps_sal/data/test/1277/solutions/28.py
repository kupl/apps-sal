from collections import deque, defaultdict
import copy


def main():
    from collections import defaultdict
    import copy
    (n, u, v) = map(int, input().split())
    u -= 1
    v -= 1
    graph = defaultdict(deque)
    for _ in range(n - 1):
        (a, b) = map(int, input().split())
        a -= 1
        b -= 1
        graph[a].append(b)
        graph[b].append(a)
    depth = dfs(graph, u, n)
    depth2 = dfs(graph, v, n)
    ans = 0
    ans2 = 10 ** 6
    for (i, j) in zip(depth, depth2):
        if i < j:
            ans = max(j, ans)
    print(ans - 1)


def dfs(G, s, n):
    stack = deque([s])
    graph = copy.deepcopy(G)
    depth = [None] * n
    depth[s] = 0
    while stack:
        u = stack[-1]
        if graph[u]:
            v = graph[u].popleft()
            if depth[v] == None:
                depth[v] = depth[u] + 1
                stack.append(v)
        else:
            stack.pop()
    return depth


main()
