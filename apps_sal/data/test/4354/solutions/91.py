N, M = map(int, input().split())
S = [tuple(map(int, input().split())) for _ in range(N)]
C = [tuple(map(int, input().split())) for _ in range(M)]
for i in S:
    ans = 0
    k = 10 ** 10
    for j in range(M):
        n = abs(i[0] - C[j][0]) + abs(i[1] - C[j][1])
        if k > n:
            k = n
            ans = j + 1
    else:
        print(ans)
