(n, k) = list(map(int, input().split()))
(a, b, c) = (2 * n, 5 * n, 8 * n)


def ceil(x, y):
    return (x + y - 1) // y


print(ceil(a, k) + ceil(b, k) + ceil(c, k))
