import math
n = int(input())
xy = []
for i in range(n):
    XY = list(map(int,input().split()))
    xy.append(XY)
total = 0
for i in range(n - 1):
    for j in range(i + 1,n):
        total += math.sqrt((xy[i][0] - xy[j][0]) ** 2 + (xy[i][1] - xy[j][1]) ** 2)
print(total * 2 / n)
