def solve(L):
    import math
    N = int(math.log2(L))
    grahp = []
    for i in range(1, N + 1):
        grahp.append([i, i + 1, 0])
        grahp.append([i, i + 1, 2 ** (i - 1)])
    for i in range(N, 0, -1):
        if L - 2 ** (i - 1) >= 2 ** N:
            L = L - 2 ** (i - 1)
            grahp.append([i, N + 1, L])
    M = len(grahp)

    print(N + 1, M)
    [print(' '.join([str(i) for i in g])) for g in grahp]


def __starting_point():
    L = int(input())
    solve(L)


__starting_point()
