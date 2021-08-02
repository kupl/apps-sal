from math import *
n, a, b = map(int, input().split())
ans = (10000005700000, 1000000000064000)
ansp = 10**55
if a * b >= 6 * n:
    ans = (a, b)
    ansp = a * b

for x in range(int(sqrt(6 * n) * 1.33)):
    yy = max(0, ceil((6 * n - a * b - b * x) / (a + x)) - 1)
    for y in range(yy, yy + 3):
        if 6 * n <= (a + x) * (b + y) < ansp:
            ansp = (a + x) * (b + y)
            ans = (a + x, b + y)
a, b = b, a
for x in range(int(sqrt(6 * n) * 1.44)):
    yy = max(0, ceil((6 * n - a * b - b * x) / (a + x)) - 1)
    for y in range(yy, yy + 3):
        if 6 * n <= (a + x) * (b + y) < ansp:
            ansp = (a + x) * (b + y)
            ans = (b + y, a + x)

print(ansp)
print(*ans)
