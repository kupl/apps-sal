from math import factorial
import sys
sys.setrecursionlimit(10 ** 4)


def comb(n, r):
    """
    >>> comb(2, 1)
    2
    >>> comb(3, 2)
    3
    """
    if r == 0:
        return 1
    if n == 0 or r > n:
        return 0
    return factorial(n) // factorial(n - r) // factorial(r)


def f(S, i, k):
    if k == 0:
        return 1
    if len(S) <= i:
        return 0
    n = int(S[i])
    if n == 0:
        return f(S, i + 1, k)
    ret = (n - 1) * comb(len(S) - i - 1, k - 1) * pow(9, k - 1)
    ret += comb(len(S) - i - 1, k) * pow(9, k)
    ret += f(S, i + 1, k - 1)
    return ret


def solve(S: str, K: int):
    return f(S, 0, K)


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = next(tokens)
    K = int(next(tokens))
    print(solve(N, K))


def test():
    import doctest
    doctest.testmod()


def __starting_point():
    test()
    main()


__starting_point()
