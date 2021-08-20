import sys
from math import gcd
from functools import reduce


def f(A):
    ret = [A[0]]
    for a in A:
        ret.append(gcd(ret[-1], a))
    ret[0] = reduce(gcd, A[1:])
    return ret


def solve(N: int, A: 'List[int]'):
    return max((gcd(g0, g1) for (g0, g1) in zip(f(A), f(A[::-1])[-2::-1])))


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))
    A = [int(next(tokens)) for _ in range(N)]
    print(solve(N, A))


def test():
    import doctest
    doctest.testmod()


def __starting_point():
    main()


__starting_point()
