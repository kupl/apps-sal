n, m = map(int, input().split())
P = [list(map(int, input().split())) for _ in range(n)]
C = [list(map(int, input().split())) for _ in range(m)]

for i in range(n):
    min_dist = 10**18
    idx = 0
    for j in range(m):
        dist = abs(P[i][0] - C[j][0]) + abs(P[i][1] - C[j][1])
        if min_dist > dist:
            idx = j + 1
            min_dist = dist
    print(idx)
