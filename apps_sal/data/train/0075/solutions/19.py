import math
T = int(input())
for _ in range(T):
    n = int(input())
    th = math.pi / (2 * n)
    l = 1.0 / math.sin(th)
    th1 = n // 2 * (2 * th)
    th = math.atan((1 - math.sin(th1)) / math.cos(th1))
    res = l * math.cos(th)
    print(res)
