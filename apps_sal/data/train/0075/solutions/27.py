import math
T = int(input())
while T != 0:
    n = int(input())
    side = math.sin(math.pi / (4 * n)) * 2
    print(1 / side)
    T -= 1
