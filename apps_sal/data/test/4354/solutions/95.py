def dist(x, y):
    return abs(x[0] - y[0]) + abs(x[1] - y[1])


N, M = list(map(int, input().split()))
AB = [list(map(int, input().split())) for _ in range(N)]
CD = [list(map(int, input().split())) for _ in range(M)]
for i in range(N):
    ans = -1
    min_dist = float("inf")
    for j in range(M):
        if (d := dist(AB[i], CD[j])) < min_dist:
            ans = j
            min_dist = d
    print((ans + 1))
