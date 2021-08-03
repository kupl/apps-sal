from math import sqrt

a, b = map(int, input().split())
n = int(input())
ans = 10 ** 20
for i in range(n):
    x, y, v = map(int, input().split())
    ans = min(ans, sqrt((x - a) ** 2 + (y - b) ** 2) / v)
print("%.10f" % ans)
