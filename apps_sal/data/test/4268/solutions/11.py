(N, D) = map(int, input().split())
X = []
for i in range(N):
    X.append(list(map(int, input().split())))
ans = 0
for i in range(N):
    for j in range(i + 1, N):
        d = 0
        for k in range(D):
            d += (X[i][k] - X[j][k]) ** 2
        d = d ** (1 / 2)
        if int(d) == d:
            ans += 1
print(ans)
