INF = 10**9

H, W = map(int, input().split())

c = [list(map(int, input().split())) for i in range(10)]

dp = [[(INF if i != j else 0) for j in range(10)]for i in range(10)]
for k in range(0, 10, 1):
    for i in range(0, 10, 1):
        for j in range(0, 10, 1):
            c[i][j] = min(c[i][j], c[i][k] + c[k][j])


A = [list(map(int, input().split())) for i in range(H)]
ans = 0
for i in range(H):
    for j in range(W):
        if A[i][j] > -1:
            ans += c[A[i][j]][1]
print(ans)
