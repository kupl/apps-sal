import sys


def f(S):
    c, n = S[0], 1
    for cc in S[1:]:
        if c == cc:
            n += 1
        else:
            yield c, n
            c, n = cc, 1
    yield c, n


def solve(N: int, K: int, S: str):
    from itertools import zip_longest
    A = list(f(S))
    M = len(A)
    i, j, k, su, ans = 0, 0, 0, 0, 0
    while i < M:
        while j < M and (k < K or A[j][0] == "1"):
            su += A[j][1]
            k += 1 if A[j][0] == "0" else 0
            j += 1
        ans = max(ans, su)
        su -= A[i][1]
        k -= 1 if A[i][0] == "0" else 0
        i += 1
    return ans


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))
    K = int(next(tokens))
    S = next(tokens)
    print((solve(N, K, S)))


def test():
    import doctest
    doctest.testmod()


def __starting_point():
    main()


__starting_point()
