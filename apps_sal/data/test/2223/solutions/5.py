# n nodes, n - 1 edges, no possibility for loop
# so no need of maintaining a vis array, it'd not visit nodes previously visited
# as long as you don't go along the edge back which leads you to the current node


from collections import deque


def main():
    n = int(input())
    # don't use hash table
    neis = [[] for i in range(n + 1)]
    vis = [0 for i in range(n + 1)]  # vis[i] -- the next node i is going to visit is neis[vis[i]]
    nodes = [1 for i in range(n + 1)]  # nodes[i] -- the number of nodes 'belong to' i(included i)
    pre = [None for i in range(n + 1)]  # pre[i] -- the node which leads to node i in fake dfs process
    cut = 0

    for _ in range(n - 1):
        u, v = list(map(int, input().split()))
        neis[u].append(v)
        neis[v].append(u)
    for i in range(1, n + 1):
        neis[i].append(None)

    start_point = 1
    q = deque()
    q.append(start_point)

    while len(q) > 0:
        top = q[-1]
        nei = neis[top][vis[top]]

        if nei is not None:
            vis[top] += 1
            if nei != pre[top]:
                q.append(nei)
                pre[nei] = top
        else:
            if top != start_point:
                nodes[pre[top]] += nodes[top]
                if nodes[top] % 2 == 0:
                    cut += 1
            q.pop()

    if nodes[1] % 2 == 0:
        print(cut)
    else:
        print(-1)


def __starting_point():
    main()


__starting_point()
