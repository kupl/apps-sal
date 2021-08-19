(N, M) = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(N)]
cd = [list(map(int, input().split())) for _ in range(M)]
for i in range(N):
    ans = -1
    dist = 10 ** 12
    for j in range(M):
        tmp = abs(ab[i][0] - cd[j][0]) + abs(ab[i][1] - cd[j][1])
        if tmp < dist:
            ans = j
            dist = tmp
    print(ans + 1)
