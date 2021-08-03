N, M = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(N)]
cd = [list(map(int, input().split())) for _ in range(M)]

for i in range(N):
    dist = float("inf")
    ans = 0
    a, b = ab[i][0], ab[i][1]

    for j in range(M)[::-1]:
        c, d = cd[j][0], cd[j][1]
        if abs(a - c) + abs(b - d) <= dist:
            dist = abs(a - c) + abs(b - d)
            ans = j + 1

    print(ans)
