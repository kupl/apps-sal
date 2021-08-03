from math import hypot, atan2

N = int(input())
engines = [tuple(map(int, input().split())) for _ in range(N)]

engines.sort(key=lambda z: atan2(z[1], z[0]))

ans = 0
for L in range(N):
    for R in range(N):
        if L <= R:
            x, y = list(map(sum, list(zip(*engines[L:R + 1]))))
        else:
            x, y = list(map(sum, list(zip(*(engines[:R + 1] + engines[L:])))))
        dist = hypot(x, y)
        ans = max(ans, dist)

print(ans)
