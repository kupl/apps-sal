import math

N, D = map(int, input().split())
Dis = []
for i in range(N):
    A = list(map(int, input().split()))
    Dis.append(A)
ans = 0
plus = 0
for m in range(N - 1):
    for k in range(N - 1):
        for j in range(D):
            B = Dis[m][j] - Dis[m + k + 1][j]
            B = B**2
            plus += B
        plus = math.sqrt(plus)
        if round(plus) == plus:
            ans += 1
        plus = 0
        if m + k + 1 == N - 1:
            break
print(ans)
