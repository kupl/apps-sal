import math

N, D = map(int, input().split())
X = [list(map(int, input().split())) for _ in range(N)]
ans = 0
for i in range(N - 1):
    for j in range(i + 1, N):
        d = 0
        for k in range(D):
            d += (X[i][k] - X[j][k]) ** 2
        if int(math.sqrt(d)) ** 2 == d:
            ans += 1
print(ans)
