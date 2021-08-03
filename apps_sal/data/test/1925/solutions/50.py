import math


def __starting_point():

    a, b, n = list(map(int, input().split()))

    ans = 0
    lp = min(b - 1, n)
    ans = math.floor((a * lp) / b) - a * math.floor(lp / b)
    print(ans)


__starting_point()
