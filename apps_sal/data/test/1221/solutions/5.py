def solve():
    N, M = list(map(int, input().split()))

    T = list(map(int, input().split()))
    B = list(map(int, input().split()))

    res = []
    for n in range(N):
        for m in range(M):
            res.append([T[n] * B[m], n, m])

    res.sort(reverse=True)

    a = T[res[0][1]]

    T.remove(a)

    MAX = (-1) * float('inf')
    for t in T:
        for b in B:
            MAX = max(t * b, MAX)

    print(int(MAX))


def __starting_point():
    solve()


__starting_point()
