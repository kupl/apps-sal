import math
n, d = list(map(int, input().split()))

cnt = 0
for i in range(n):
    x, y = list(map(int, input().split()))
    dist = math.sqrt(x**2 + y**2)

    if dist <= d:
        cnt += 1

print(cnt)
