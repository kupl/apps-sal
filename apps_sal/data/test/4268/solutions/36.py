import math
(N, D) = list(map(int, input().split()))
X = [list(map(int, input().split())) for _ in range(N)]


def check(i, j):
    dis = 0
    for k in range(D):
        dis += (X[i][k] - X[j][k]) ** 2
    if int(math.sqrt(dis)) ** 2 == dis:
        return 1
    else:
        return 0


ans = 0
for i in range(N):
    for j in range(i + 1, N):
        ans += check(i, j)
print(ans)
