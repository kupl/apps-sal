import sys


def f(n, N, K):
    '''
    >>> f(2, 10, 2)
    0
    >>> f(1, 10, 0)
    10
    >>> f(1, 10, 1)
    0
    >>> f(2, 10, 1) 
    5
    >>> f(3, 10, 0) 
    10
    >>> f(3, 10, 1) 
    7
    >>> f(3, 10, 2) 
    3
    >>> f(5, 5, 2)
    3
    '''
    if n <= K:
        return 0
    if K == 0:
        return N
    ans = max(N % n - (K - 1), 0)
    ans += N // n * (n - K)
    return ans


def solve(N: int, K: int):
    ans = 0
    for b in range(N + 1):
        ans += f(b, N, K)
    return ans


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))
    K = int(next(tokens))
    print((solve(N, K)))


def test():
    import doctest
    doctest.testmod()


def __starting_point():
    test()
    main()


__starting_point()
