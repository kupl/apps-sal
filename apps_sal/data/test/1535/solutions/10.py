import math
(n, x0, y0) = list(map(int, input().split()))
slope = []
for i in range(n):
    (x1, y1) = list(map(int, input().split()))
    if x1 == x0:
        slp = 999
    else:
        slp = (y1 - y0) / (x1 - x0)
    slope.append(slp)
slope.sort()
count = 1
point = slope[0]
for i in range(1, len(slope)):
    if slope[i] == point:
        continue
    else:
        count += 1
        point = slope[i]
print(count)
