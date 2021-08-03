def main():
    n, m, k = map(int, input().split())
    graph = [[] for i in range(n + 1)]
    for i in range(m):
        u, v, l = map(int, input().split())
        graph[u].append((v, l))
        graph[v].append((u, l))

    if k == 0:
        print(-1)
        return

    a = list(map(int, input().split()))
    check = [True for i in range(n + 1)]
    for x in a:
        check[x] = False
    ans = 10 ** 10
    for x in a:
        if graph[x] != []:
            for y in graph[x]:
                if check[y[0]]:
                    ans = min(ans, y[1])

    if ans == 10 ** 10:
        ans = -1
    print(ans)


def __starting_point():
    main()


__starting_point()
