def abc073_d():
    from scipy.sparse import lil_matrix
    from scipy.sparse.csgraph import floyd_warshall
    from itertools import permutations

    n, m, r = map(int, input().split())
    R = list(map(lambda x: int(x) - 1, input().split()))
    graph = lil_matrix((n, n), dtype=int)
    for _ in range(m):
        a, b, c = map(int, input().split())
        a -= 1
        b -= 1
        graph[a, b] = c
        graph[b, a] = c

    dist = floyd_warshall(csgraph=graph)

    ans = 10**18
    for route in permutations(R, r):
        tmp = 0
        for i in range(r - 1):
            s = route[i]
            t = route[i + 1]
            tmp += dist[s][t]
            if tmp > ans:
                break
        ans = min(ans, tmp)

    print(int(ans))


def __starting_point():
    abc073_d()


__starting_point()
