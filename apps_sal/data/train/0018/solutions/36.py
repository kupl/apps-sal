import math
T = int(input())
n = [0] * T
m = [0] * T
a = [0] * T
p = [0] * T
for t in range(T):
    n = 2 * int(input())
    out = 0
    if n % 4 == 0:
        print(math.tan(math.pi / n) ** (-1))
    else:
        print(math.sin(math.pi / n) ** (-1))
