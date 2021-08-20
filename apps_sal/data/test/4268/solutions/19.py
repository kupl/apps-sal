import math
(n, d) = map(int, input().split())
x = [list(map(int, input().split())) for i in range(n)]
cnt = 0
for i in range(n):
    for j in range(i + 1, n):
        dis = 0
        for k in range(d):
            dis += (x[i][k] - x[j][k]) ** 2
        if math.sqrt(dis) % 1 == 0:
            cnt += 1
print(cnt)
