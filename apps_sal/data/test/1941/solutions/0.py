import sys
import math


a, b, n = list(map(int, str.split(sys.stdin.readline())))
def s(i): return a + (i - 1) * b
def S(i): return a * i + b * i * (i - 1) // 2


for _ in range(n):

    l, t, m = list(map(int, str.split(sys.stdin.readline())))

    d = (b / 2 - a) ** 2 + 4 * b / 2 * (m * t + S(l - 1))
    if d < 0:

        print(-1)
        continue

    r = min(
        math.floor((t - a) / b + 1),
        math.floor(((b / 2 - a) + math.sqrt(d)) / b)
    )
    if r < l:

        print(-1)

    else:

        print(r)
