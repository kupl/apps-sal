nax = 150123
edges = [[] for _ in range(nax)]
vis = [False for j in range(nax)]


def dfs(a, cnt_vertices, cnt_edges):
    stack = [a]
    while len(stack) > 0:
        a = stack.pop()
        if vis[a]:
            continue
        vis[a] = True
        cnt_vertices[0] += 1
        cnt_edges[0] += len(edges[a])
        for b in edges[a]:
            if not vis[b]:
                stack.append(b)


def main():
    (n, m) = list(map(int, str(input()).strip().split()))
    for _ in range(m):
        (a, b) = list(map(int, str(input()).strip().split()))
        edges[a].append(b)
        edges[b].append(a)
    for i in range(1, n + 1):
        if not vis[i]:
            cnt_vertices = [0]
            cnt_edges = [0]
            dfs(i, cnt_vertices, cnt_edges)
            if cnt_edges[0] != cnt_vertices[0] * (cnt_vertices[0] - 1):
                print('NO')
                return 0
    print('YES')


def __starting_point():
    main()


__starting_point()
