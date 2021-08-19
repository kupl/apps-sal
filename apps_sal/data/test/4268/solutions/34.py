import math
(N, D) = list(map(int, input().split()))
Xarray = [list(map(int, input().split())) for _ in range(N)]
ans = 0
for i in range(N - 1):
    for j in range(i + 1, N):
        sum = 0
        for k in range(D):
            sum += abs(Xarray[i][k] - Xarray[j][k]) ** 2
        if math.sqrt(sum).is_integer():
            ans += 1
print(ans)
