def dfs(start):
    visited = [0, True] + [False] * (n - 1)
    stack = [(x, 1, 1 / len(tree[start])) for x in tree[start]]
    while stack:
        v, l, p = stack.pop()
        if leafs[v]:
            L.append(l * p)
        if not visited[v]:
            visited[v] = True
            for u in tree[v]:
                if not visited[u]:
                    stack.append((u, l + 1, p / (len(tree[v]) - 1)))


n = int(input())
tree = {x: [] for x in range(1, n + 1)}
L = []
for _ in range(n - 1):
    u, v = list(map(int, input().split()))
    tree[u].append(v)
    tree[v].append(u)
leafs = [False, True] + [len(tree[x]) == 1 for x in range(2, n + 1)]
dfs(1)
print(sum(L))

"""
7
1 2
1 3
1 4
4 7
2 6
2 5
"""
