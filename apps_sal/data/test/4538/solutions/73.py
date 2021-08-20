import math
(N, D) = list(map(int, input().split()))
XY = [list(map(int, input().split())) for _ in range(N)]
count = 0
for (x, y) in XY:
    if math.sqrt(x ** 2 + y ** 2) <= D:
        count += 1
print(count)
