import math

N, D = list(map(int, input().split()))
cnt = 0
for i in range(N):
    x, y = list(map(int, input().split()))
    distance = math.sqrt(x*x + y*y)

    if distance <= D:
        cnt += 1

print(cnt)

