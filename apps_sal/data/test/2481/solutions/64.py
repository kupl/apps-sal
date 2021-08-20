(H, W) = list(map(int, input().split()))
cost = [list(map(int, input().split())) for i in range(10)]
A = [list(map(int, input().split())) for i in range(H)]
for k in range(10):
    for i in range(10):
        for j in range(10):
            cost[i][j] = min(cost[i][j], cost[i][k] + cost[k][j])
ans = 0
for i in range(H):
    for j in range(W):
        now = A[i][j]
        if now != -1:
            ans += cost[now][1]
print(ans)
