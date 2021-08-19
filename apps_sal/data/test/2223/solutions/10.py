
def main():
    n = int(input())

    g = [[] for i in range(n + 5)]
    vh = [[] for i in range(n + 5)]
    size = [1 for i in range(n + 5)]
    par = [i for i in range(n + 5)]

    if n % 2 == 1:
        print(-1)
        return

    for i in range(n - 1):
        u, v = map(int, input().split())
        g[u].append(v)
        g[v].append(u)

    q = [[1, 1]]
    vh[1].append(1)
    max_height = 1
    while len(q) > 0:
        u, hu = q.pop()
        # print(u)
        leaf_node = True

        for v in g[u]:
            if v == par[u]:
                continue
            hv = hu + 1
            par[v] = u
            q.append([v, hv])
            vh[hv].append(v)
            max_height = max(max_height, hv)

    while max_height > 0:
        for v in vh[max_height]:
            size[par[v]] += size[v]
        max_height -= 1

    print(n - 1 - sum(size[i] % 2 for i in range(1, n + 1)))


main()
