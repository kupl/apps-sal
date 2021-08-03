import itertools
import math


S = 1000000


def __starting_point():
    fact = list(itertools.accumulate(list(range(S + 1)), lambda x, y: x + math.log(y)))
    n, m = [int(x) for x in input().split()]
    res = 0.0
    for i in range(1, min(n, m) + 1):
        res += math.exp(
            math.log(n) + (fact[m] - fact[i] - fact[m - i])
            + (fact[(n - 1) * m] - fact[n - i] - fact[(n - 1) * m - n + i])
                        - (fact[n * m] - fact[n] - fact[n * m - n])
            + math.log((1.0 * i / n) ** 2))
    print(res)


__starting_point()
