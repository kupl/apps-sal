import math
N = int(input())
m = 10 ** 18
for x in range(1, N + 1):
    y = math.ceil(N / x)
    if 2 * (x + y) < m:
        (a, b) = (x, y)
        m = 2 * (x + y)
    x += 1
print(2 * (a + b))
