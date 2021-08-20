def f(b, n):
    return n if n < b else n % b + f(b, n // b)


def solve():
    (N, S) = map(int, open(0))
    if N == S:
        return N + 1
    sqr = int(N ** 0.5)
    for b in range(2, sqr + 1):
        if f(b, N) == S:
            return b
    M = N - S
    for p in reversed(range(1, sqr + 1)):
        b = M // p + 1
        if b >= 2 and f(b, N) == S:
            return b
    return -1


print(solve())
