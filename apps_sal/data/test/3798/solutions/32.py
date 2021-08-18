import sys


def f(n, b):
    if n < b:
        return n
    else:
        return n % b + f(n // b, b)


def solve(n: int, s: int):
    if s > n:
        return -1

    if s == n:
        return n + 1

    b = 2
    while b * b <= n:
        if f(n, b) == s:
            return b
        b += 1

    for p in range(b - 1, 0, -1):
        if (n - s) % p > 0:
            continue

        c = (n - s) // p + 1
        if f(n, c) == s:
            return c

    return -1


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    n = int(next(tokens))
    s = int(next(tokens))
    print((solve(n, s)))


def __starting_point():
    main()


__starting_point()
