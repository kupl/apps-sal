def main():
    INF = float('inf')
    (N, M, P, *ABC) = list(map(int, open(0).read().split()))
    F = [[] for _ in range(N)]
    B = [[] for _ in range(N)]
    E = [(a - 1, b - 1, P - c) for (a, b, c) in zip(*[iter(ABC)] * 3)]
    for (a, b, c) in E:
        F[a].append(b)
        B[b].append(a)

    def reachable(E, a):
        S = {a}
        stack = [a]
        while stack:
            s = stack.pop()
            for v in E[s]:
                if v not in S:
                    stack.append(v)
                    S.add(v)
        return S
    ok = reachable(F, 0) & reachable(B, N - 1)
    E = [(a, b, c) for (a, b, c) in E if a in ok and b in ok]
    D = [INF] * N
    D[0] = 0

    def bellman_ford(N):
        for _ in range(N):
            update = False
            for (a, b, c) in E:
                if D[b] > D[a] + c:
                    D[b] = D[a] + c
                    update = True
            if not update:
                return False
        return True
    print(-1 if bellman_ford(N + 1) else max(-D[-1], 0))


def __starting_point():
    main()


__starting_point()
