import math
n = int(input())
x = math.floor((-1 + math.sqrt(8 * n + 9)) / 2)
for i in range(x + 3, x - 2, -1):
    if (n + 2) * (n + 1) - i * (i + 1) >= n * (n + 1):
        y = i
        break
print(n + 1 - y)
