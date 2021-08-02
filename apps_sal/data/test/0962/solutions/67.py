import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N, M, *AB = list(map(int, read().split()))
    G = [[] for _ in range(N)]
    for a, b in zip(*[iter(AB)] * 2):
        G[a - 1].append(b - 1)

    def dfs(v, p, seen, finished, hist):
        seen[v] = True
        hist.append(v)
        for nv in G[v]:
            if nv == p:
                continue
            if finished[nv]:
                continue
            if seen[nv] and not finished[nv]:
                return nv

            pos = dfs(nv, v, seen, finished, hist)
            if pos != -1:
                return pos
        hist.pop()
        finished[v] = True
        return -1

    for i in range(N):
        seen = [False] * N
        finished = [False] * N
        hist = []
        pos = dfs(i, -1, seen, finished, hist)
        if pos != -1:
            break

    if pos == -1:
        print((-1))
        return

    cycle = []
    while hist:
        t = hist.pop()
        cycle.append(t)
        if t == pos:
            break

    cycle.reverse()

    while True:
        order = [-1] * N
        for i, v in enumerate(cycle):
            order[v] = i

        for i, v in enumerate(cycle):
            ord_from = ord_to = -1
            for nv in G[v]:
                if v == nv or order[nv] == -1 or order[nv] == (order[v] + 1) % len(cycle):
                    continue
                ord_from, ord_to = i, order[nv]
                break
            if ord_from != -1:
                break

        if ord_from == -1:
            break

        if ord_from < ord_to:
            cycle = cycle[: ord_from + 1] + cycle[ord_to:]
        else:
            cycle = cycle[ord_to: ord_from + 1]

    print((len(cycle)))
    for v in cycle:
        print((v + 1))

    return


def __starting_point():
    main()


__starting_point()
