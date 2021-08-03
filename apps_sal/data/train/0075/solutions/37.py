import math
for ad in range(int(input())):
    n = int(input())
    n *= 2
    t = math.pi / n
    x = math.cos(t / 2) / (2 * math.sin(t))
    print(2 * x)
