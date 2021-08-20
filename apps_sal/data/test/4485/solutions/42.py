import sys
YES = 'POSSIBLE'
NO = 'IMPOSSIBLE'


def solve(N: int, M: int, a: 'List[int]', b: 'List[int]'):
    AB = sorted(zip(a, b))
    s = set([b for (a, b) in AB if a == 1])
    g = set([a for (a, b) in AB if b == N])
    return YES if s & g else NO


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))
    M = int(next(tokens))
    a = [int()] * M
    b = [int()] * M
    for i in range(M):
        a[i] = int(next(tokens))
        b[i] = int(next(tokens))
    print(solve(N, M, a, b))


def test():
    import doctest
    doctest.testmod()


def perf():
    import cProfile
    cProfile.run('main()')


def __starting_point():
    main()


__starting_point()
