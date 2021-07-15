import math
n, d = map(int, input().split())
s = 0
for i in range(n):
    x, y = map(int, input().split())
    r = x**2 + y**2
    if r<=d**2:
        s += 1

print(s)
