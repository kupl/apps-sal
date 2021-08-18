import sys
from collections import deque


def solve(N: int, M: int, G, S: int, T: int):
    S -= 1
    T -= 1
    now = deque([S])
    dist = [0 for _ in range(N * 3)]
    while now:
        p = now.popleft()
        for n in G[p]:
            if dist[n] != 0:
                continue
            dist[n] = dist[p] + 1
            if n == T:
                print((dist[n] // 3))
                return
            now.append(n)
    print((-1))
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))
    M = int(next(tokens))
    G = tuple(set() for _ in range(N * 3))
    for _ in range(M):
        u, v = int(next(tokens)) - 1, int(next(tokens)) - 1
        G[u].add(v + N)
        G[u + N].add(v + 2 * N)
        G[u + 2 * N].add(v)

    S = int(next(tokens))
    T = int(next(tokens))
    solve(N, M, G, S, T)


def __starting_point():
    main()


__starting_point()
