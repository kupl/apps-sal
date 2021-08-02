N, X, Y = map(int, input().split())
X -= 1; Y -= 1
ans = [0 for _ in range(N - 1)]
for i in range(N):
    for j in range(i + 1, N):
        direct = j - i
        shortcut = abs(X - i) + 1 + abs(Y - j)
        shortest = min(direct, shortcut)
        ans[shortest - 1] += 1
print(*ans, sep="\n")
