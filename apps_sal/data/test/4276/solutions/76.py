(N, T) = map(int, input().split())
CT = [tuple(map(int, input().split())) for _ in range(N)]
res = 1001
for (c, t) in CT:
    if t <= T:
        res = min(res, c)
print(res if res <= 1000 else 'TLE')
