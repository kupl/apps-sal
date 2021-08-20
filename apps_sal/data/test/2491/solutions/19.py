import sys
sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    (N, M) = list(map(int, rl().split()))
    graph = []
    for _ in range(M):
        (a, b, c) = list(map(int, rl().split()))
        a -= 1
        b -= 1
        c *= -1
        graph.append([a, b, c])

    def bellman_ford(s):
        dist_ls = [10 ** 15] * N
        dist_ls[s] = 0
        for i in range(N):
            for (s, t, w) in graph:
                if dist_ls[s] + w < dist_ls[t]:
                    dist_ls[t] = dist_ls[s] + w
                    if i == N - 1 and t == N - 1:
                        return -1
        return dist_ls
    dist = bellman_ford(0)
    if dist == -1:
        print('inf')
    else:
        print(-1 * dist[-1])


def __starting_point():
    solve()


__starting_point()
