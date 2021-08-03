N = 10
MAX_C = 1000


H, W = [int(x) for x in input().split()]
C = [[int(x) for x in input().split()] for _ in range(N)]
dist = [0 if i == 1 else MAX_C for i in range(N)]


def bellman_ford():
    for _ in range(N - 1):
        for u in range(N):
            for v in range(N):
                dist[v] = min(dist[v], dist[u] + C[v][u])


bellman_ford()
ans = sum([sum([0 if x == "-1" else dist[int(x)] for x in input().split()]) for _ in range(H)])
print(ans)
