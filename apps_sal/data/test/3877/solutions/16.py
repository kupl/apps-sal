def main():
    n, l, r = list(map(int, input().split()))

    c = n
    h = 0
    while c > 0:
        h += 1
        c //= 2
    c = 2 ** h - 1

    print(ones(n, c, l-1, r-1))


def ones(n, c, l, r):
    if n == 1:
        return 1

    if n == 0:
        return 0

    if l == 0 and r == c-1:
        return n

    m = c // 2
    total = 0

    if l < m < r:
        # [l, m-1] + [m+1, r] + [m]
        total = ones(n // 2, m, l, m - 1) + ones(n // 2, m, 0, r - m - 1) + (1 if n % 2 == 1 else 0)
    elif l < r < m:
        # [l, r]
        total = ones(n // 2, m, l, r)
    elif m < l < r:
        # [l, r]
        total = ones(n // 2, m, l - m - 1, r - m - 1)
    elif l == m < r:
        # [m+1, r] + m
        total = ones(n // 2, m, 0, r - m - 1) + (1 if n % 2 == 1 else 0)
    elif l < m == r:
        # [l, m] + m
        total = ones(n // 2, m, l, m) + (1 if n % 2 == 1 else 0)
    elif l == r < m:
        total = ones(n // 2, m, l, r)
    elif m < l == r:
        total = ones(n // 2, m, l - m - 1, r - m - 1)
    elif l == m == l:
        total = (1 if n % 2 == 1 else 0)

    return total


def __starting_point():
    main()

__starting_point()
