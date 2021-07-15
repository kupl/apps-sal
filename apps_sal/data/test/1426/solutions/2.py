import sys
from collections import deque

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N, M = list(map(int, readline().split()))
    G = [[] for _ in range(N)]
    for _ in range(M):
        u, v = list(map(int, readline().split()))
        G[u - 1].append(v - 1)
    S, T = list(map(int, readline().split()))
    S -= 1
    T -= 1

    dist = [[-1] * 3 for _ in range(N)]
    dist[S][0] = 0
    queue = deque([(S, 0)])
    while queue:
        v, step = queue.popleft()
        if step == 0 and v == T:
            break

        for nv in G[v]:
            if dist[nv][(step - 1) % 3] != -1:
                continue
            dist[nv][(step - 1) % 3] = dist[v][step] + 1
            queue.append((nv, (step - 1) % 3))

    if dist[T][0] == -1:
        print((-1))
    else:
        print((dist[T][0] // 3))
    return


def __starting_point():
    main()

__starting_point()
