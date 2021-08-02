def main():
    INF = float("inf")

    N, M, P, *ABC = list(map(int, open(0).read().split()))

    F = [[] for _ in range(N)]
    B = [[] for _ in range(N)]
    E = [(a - 1, b - 1, P - c) for a, b, c in zip(*[iter(ABC)] * 3)]

    for a, b, c in E:
        F[a].append(b)
        B[b].append(a)

    S = {0}
    stack = [0]
    while stack:
        s = stack.pop()
        for v in F[s]:
            if v not in S:
                stack.append(v)
                S.add(v)

    T = {N - 1}
    stack = [N - 1]
    while stack:
        s = stack.pop()
        for v in B[s]:
            if v not in T:
                stack.append(v)
                T.add(v)

    ok = S & T

    E = [(a, b, c) for a, b, c in E if a in ok and b in ok]

    D = [INF] * N
    D[0] = 0

    def bellman_ford(N):
        for _ in range(N):
            update = False
            for a, b, c in E:
                if D[b] > D[a] + c:
                    D[b] = D[a] + c
                    update = True
            if not update:
                return False
        return True

    bellman_ford(N)

    print((-1 if bellman_ford(1) else max(-D[-1], 0)))


def __starting_point():
    main()


__starting_point()
