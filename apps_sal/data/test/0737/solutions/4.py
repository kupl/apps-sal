import math
n = int(input())
mn = 2 * n + 2
for i in range(n, min(4 * n, n + 1000)):
    s = int(math.sqrt(i))
    for j in range(s, 0, -1):
        if i % j == 0:
            mn = min(mn, 2 * (j + i // j))
            break
print(mn)
