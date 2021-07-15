import math

T = int(input())
for t in range(T):
    n, x = map(int, input().split())
    gs = [tuple(map(int, input().split())) for _ in range(n)]
    max_d = max(g[0] for g in gs)
    max_delta = max(g[0] - g[1] for g in gs)
    if x <= max_d:
        c = 1
    elif max_delta <= 0:
        c = -1
    else:
        c = math.ceil((x - max_d)/max_delta) + 1
    print(c)
