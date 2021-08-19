def main():
    (n, m) = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in [0] * m]
    g = [set() for _ in [0] * n]
    g2 = [set() for _ in [0] * n]
    [g[a - 1].add(b - 1) for (a, b) in ab]
    [g2[b - 1].add(a - 1) for (a, b) in ab]

    def bfs(start, graph):
        temp = [[start, {start}]]
        while temp:
            temp2 = []
            for (j, k) in temp:
                for i in graph[j]:
                    if i in k:
                        return (j, k)
                    else:
                        temp2.append([i, k | {i}])
            temp = temp2
        return (None, None)
    return_set_pre = set(range(n))
    for i in range(n):
        (now, return_set) = bfs(i, g)
        if return_set != None:
            break
    if return_set == None:
        print(-1)
        return 0
    while True:
        for i in return_set_pre - return_set:
            g[i] = {}
            g2[i] = {}
        for i in return_set:
            g[i] = g[i] & return_set
            g2[i] = g2[i] & return_set
        l1 = len([1 for i in range(n) if len(g[i]) == 1])
        l2 = len([1 for i in range(n) if len(g2[i]) == 1])
        l = len(return_set)
        if l == l1 and l == l2:
            break
        return_set_pre = return_set
        (now, return_set) = bfs(now, g2)
        for i in return_set_pre - return_set:
            g[i] = {}
            g2[i] = {}
        for i in return_set:
            g[i] = g[i] & return_set
            g2[i] = g2[i] & return_set
        l1 = len([1 for i in range(n) if len(g[i]) == 1])
        l2 = len([1 for i in range(n) if len(g2[i]) == 1])
        l = len(return_set)
        if l == l1 and l == l2:
            break
        return_set_pre = return_set
        (now, return_set) = bfs(now, g)
    print(len(return_set))
    for i in return_set:
        print(i + 1)


main()
