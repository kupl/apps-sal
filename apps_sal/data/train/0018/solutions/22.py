import math
t = int(input())


for ti in range(t):
    n = int(input())
    a = math.pi / (2 * n)
    side = (1 / math.tan(a))
    print(side)
