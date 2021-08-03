import sys
from collections import deque

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

    ans = []
    for i in range(N):
        queue = deque([i])
        dist = [-1] * N
        dist[i] = 0
        prev = [-1] * N
        while queue:
            v = queue.popleft()
            for nv in G[v]:
                if dist[nv] == -1:
                    dist[nv] = dist[v] + 1
                    prev[nv] = v
                    queue.append(nv)
        for j in range(N):
            if i == j or dist[j] == -1 or i not in G[j]:
                continue
            tmp = []
            k = j
            while k != -1:
                tmp.append(k)
                k = prev[k]

            if not ans or len(ans) > len(tmp):
                ans = tmp

    if ans:
        print((len(ans)))
        for v in ans:
            print((v + 1))
    else:
        print((-1))

    return


def __starting_point():
    main()


__starting_point()
