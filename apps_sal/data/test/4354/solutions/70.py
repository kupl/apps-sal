N, M = list(map(int, input().split()))
ab = list(list(map(int, input().split())) for _ in range(N))
cd = list(list(map(int, input().split())) for _ in range(M))

for i in range(N):
    k = 0
    d = abs(ab[i][0] - cd[0][0]) + abs(ab[i][1] - cd[0][1])
    for j in range(1, M):
        if abs(ab[i][0] - cd[j][0]) + abs(ab[i][1] - cd[j][1]) < d:
            k = j
            d = abs(ab[i][0] - cd[j][0]) + abs(ab[i][1] - cd[j][1])
    print((k + 1))
