import math
(N, D) = list(map(int, input().split()))
sq = [list(map(int, input().split())) for i in range(N)]
ans = 0
for j in range(N - 1):
    for k in range(j + 1, N):
        s = 0
        for l in range(D):
            s += (sq[j][l] - sq[k][l]) ** 2
        if math.sqrt(s) % 1 == 0.0:
            ans += 1
print(ans)
