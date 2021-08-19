import math
for _ in range(int(input())):
    n = int(input())
    n = 2 * n
    L = 1 / math.sin(math.pi / (2 * n)) * abs(math.sin(math.pi * (n - 1) / 4 * n))
    print(L / 2)
