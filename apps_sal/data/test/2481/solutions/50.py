h, w = list(map(int, input().split()))
c = [list(map(int, input().split())) for _ in range(10)]
a = [list(map(int, input().split())) for _ in range(h)]


def warshall_floyd(adj_m):
    # _dist[i][j] : i から j への最短距離
    _dist = adj_m
    for _k in range(10):
        for _i in range(10):
            for _j in range(10):
                _dist[_i][_j] = min(_dist[_i][_j], _dist[_i][_k] + _dist[_k][_j])
    return _dist


dist = warshall_floyd(c)

ans = 0
for i in range(h):
    for j in range(w):
        if a[i][j] != -1:
            ans += dist[a[i][j]][1]
print(ans)
