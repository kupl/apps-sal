def dfs(g, s):
    visited = set([s])
    stack = [s]
    res = 0

    while len(stack) > 0:
        s = stack.pop()
        cnt = 0

        cnt += 1  # count the size of the current subtree
        visited.add(s)

        for v in g[s]:
            if v not in visited:
                cnt += 1
                stack.append(v)

        if cnt % 2 == 0:
            res += 1

    return res // 2


def dfs2(g, s, n):
    parent = [0] * (n + 1)
    counts = [1] * (n + 1)
    stack = []

    stack.append(s)

    while stack:
        v = stack[-1]
        empty_s = True

        if not parent[v]:
            parent[v] = 1

        for node in g[v]:
            if not parent[node]:
                parent[node] = v
                stack.append(node)
                empty_s = False

        if empty_s:
            stack.pop()
            counts[parent[v]] += counts[v]

    return sum([1 for x in counts[2:] if x % 2 == 0])


def solve():
    #f = open("Cut em all - DFS.txt")
    n = int(input())

    tree = [[] for i in range(n + 1)]

    for i in range(n - 1):
        u, v = input().split()
        u, v = int(u), int(v)
        tree[v].append(u)
        tree[u].append(v)

    if n % 2 != 0:
        print(-1)
        return

    #print (dfs(tree, 1))
    print(dfs2(tree, 1, n))


def __starting_point():
    solve()


__starting_point()
