N, M = [int(c) for c in input().split()]
ab = [list(map(int, input().split())) for c in range(N)]
cd = [list(map(int, input().split())) for c in range(M)]
for i in range(N):
    mi = 2 * 10**9
    for j in range(M):
        tmp = abs(ab[i][0] - cd[j][0]) + abs(ab[i][1] - cd[j][1])
        if mi > tmp:
            mi = tmp
            ans = j + 1
    print(ans)
