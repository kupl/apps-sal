import sys


def solve(N: int, A: 'List[int]'):
    (ans, t, s) = (0, 0, 0)
    for h in range(N):
        while t < N and s ^ A[t] == s + A[t]:
            s += A[t]
            t += 1
        ans += t - h
        s -= A[h]
    return ans


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
