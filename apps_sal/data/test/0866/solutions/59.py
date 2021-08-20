def combination(N: int, R: int, MOD: int):
    """
    Return the number of combinations of N things taken R at a time
    Parameters
    ----------
    N : int
        Number of thing
    R : int
        Number of elements taken
    MOD : int
        MOD
    """
    if N - R < R:
        R = N - R
    if R == 0:
        return 1
    if R == 1:
        return N
    numerator = [N - R + r for r in range(1, R + 1)]
    denominator = [r for r in range(1, R + 1)]
    for p in range(2, R + 1):
        pivot = denominator[p - 1]
        if pivot <= 1:
            continue
        offset = (N - R) % p
        for r in range(p - 1, R, p):
            numerator[r - offset] /= pivot
            denominator[r] /= pivot
    result = 1
    for n in numerator:
        if n <= 1:
            continue
        result *= int(n)
        result %= MOD
    return result


def main():
    (X, Y) = list(map(int, input().split()))
    MOD = 10 ** 9 + 7
    n = (2 * Y - X) // 3
    m = (2 * X - Y) // 3
    if n < 0 or m < 0 or (X + Y) % 3:
        print(0)
    else:
        print(combination(n + m, n, MOD))


def __starting_point():
    main()


__starting_point()
