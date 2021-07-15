import math
n, d = map(int, input().split())

ans = 0
for i in range(n):
    x, y = map(int, input().split())
    s = math.sqrt(x ** 2 + y ** 2)
    if s <= d:
        ans += 1

print(ans) 
