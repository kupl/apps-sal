import math

N, D = map(int, input().split())
xy = [list(map(int, input().split())) for xy in range(N)]

count = 0
for i in range(N):
    l = math.sqrt(xy[i][0]**2 + xy[i][1]**2)
    if l <= D:
        count += 1

print(count)
