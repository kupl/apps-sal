import math
N = int(input())
n = 1000
x = [None] * N
y = [None] * N
for i in range(N):
    (x[i], y[i]) = list(map(int, input().split()))
ans = 0
for i in range(n):
    theta = 2 * math.pi / n * i
    tmp_x = 0
    tmp_y = 0
    for j in range(N):
        if x[j] * math.cos(theta) + y[j] * math.sin(theta) > 0:
            tmp_x += x[j]
            tmp_y += y[j]
    if tmp_x ** 2 + tmp_y ** 2 > ans ** 2:
        ans = math.sqrt(tmp_x ** 2 + tmp_y ** 2)
print(ans)
