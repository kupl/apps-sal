import math
for _ in range(int(input())):
    x, y, p, q = [int(x) for x in input().split()]
    print(math.ceil(max((y - x) / (q - p), x / p, y / q)) * q - y) if p % q else print(0) if (x * q == p * y) else print(-1)
