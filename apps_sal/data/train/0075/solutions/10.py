import math
for _ in range(int(input())):
    n = 2 * int(input())
    print(math.cos(math.pi / (2 * n)) / math.sin(math.pi / n))
