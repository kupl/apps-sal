import math

N, D = list(map(int, input().split()))
L = []
ans = 0
for _ in range(N):
    X = list(map(int, input().split()))
    L.append(X)
for i in range(N - 1):
    for j in range(i + 1, N):
        con = 0
        for k in range(D):
            con += (L[i][k] - L[j][k]) ** 2
        if int(math.sqrt(con)) ** 2 == con:
            ans += 1

print(ans)
