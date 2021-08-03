N, M = map(int, input().split())
X = []
for i in range(N):
    a, b = map(int, input().split())
    X.append((a, b))
C = []
for i in range(M):
    c, d = map(int, input().split())
    C.append((c, d))
ans = [0 for _ in range(N)]
INF = float("inf")
for i in range(N):
    MIN = INF
    check = -1
    for y in range(M):
        temp = abs(X[i][0] - C[y][0]) + abs(X[i][1] - C[y][1])
        if temp < MIN:
            MIN = temp
            check = y + 1
    ans[i] = check
print(*ans, sep="\n")
