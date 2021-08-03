import math

n = int(input())
xy = []
for i in range(n):
    xy.append(list(map(int, input().split())))
ans = 0
for j in range(n):
    for i in range(n):
        ans += math.sqrt((xy[i][0] - xy[j][0])**2 + (xy[i][1] - xy[j][1])**2)

print(ans / n)
