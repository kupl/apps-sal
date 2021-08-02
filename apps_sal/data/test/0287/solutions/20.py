n, k = map(int, input().split())


def min(a, b):
    if a < b:
        return a
    return b


if k == 0:
    print(0, 0)
else:
    print(min(n - k, 1), min(n - k, 2 * k))
