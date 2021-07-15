import math

n = int(input())

xy = []

for i in range(n):
    xy.append(list(map(int, input().split())))

ans = 0

for j in range(n):
    for k in range(n):
        ans += math.sqrt((xy[k][0] - xy[j][0]) ** 2 + (xy[k][1] - xy[j][1]) ** 2)

print(ans / n)
