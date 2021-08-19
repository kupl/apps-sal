(N, T) = map(int, input().split())
routes = [tuple(map(int, input().split())) for _ in range(N)]
res = 1001
for i in range(N):
    if routes[i][1] <= T:
        res = min(res, routes[i][0])
print([res, 'TLE'][res > 1000])
