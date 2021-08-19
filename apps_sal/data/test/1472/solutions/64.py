(N, X, Y) = map(int, input().split())
ans = [0] * (N + 1)
for i in range(1, N):
    for j in range(i + 1, N + 1):
        shortest = min(j - i, 1 + abs(X - i) + abs(Y - j))
        ans[shortest] += 1
for k in range(1, N):
    print(ans[k])
