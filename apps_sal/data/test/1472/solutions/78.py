N, X, Y = map(int, input().split())

ans = [0] * (N + 1)

for i in range(1, N):
    for j in range(i + 1, N + 1):
        dis1 = j - i
        dis2 = abs(X - i) + 1 + abs(Y - j)
        dis3 = abs(Y - i) + 1 + abs(X - j)
        d = min(dis1, dis2, dis3)
        ans[d] += 1

for i in range(1, N):
    print(ans[i])
