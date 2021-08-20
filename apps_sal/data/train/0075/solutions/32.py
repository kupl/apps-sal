import math
import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    a = 1.0 / (2.0 * math.tan(math.pi / (n * 2)))
    b = 1.0 * math.sin(math.pi / 2.0) / math.sin(math.pi / (n * 2))
    if n % 2 == 0:
        print(a * 2.0)
    else:
        rotation = [math.pi * 2.0 / (2 * n) * item for item in range(2 * n)]
        l = 0.0
        r = math.pi / 2.0
        eps_rot = [math.pi * 2.0 / (2 * n) / 10 ** 2 * item for item in range(10 ** 2)]
        ret = b
        for eps in eps_rot:
            max_rad = 0.0
            for rad in rotation:
                val = max(b * abs(math.sin(rad + eps)), b * abs(math.cos(rad + eps)))
                max_rad = max(max_rad, val)
            ret = min(ret, max_rad)
        print(ret)
