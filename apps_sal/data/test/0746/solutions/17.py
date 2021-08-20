import math
[a, b] = [int(x) for x in input().split()]
n = int(input())
ans = 1000
for i in range(n):
    [x, y, v] = [int(x) for x in input().split()]
    ans = min(ans, math.sqrt((x - a) * (x - a) + (y - b) * (y - b)) / v)
print(ans)
