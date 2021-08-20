(a, b, x) = map(int, input().split())


def cntr(n, x):
    if n >= 0:
        return n // x + 1
    else:
        return 0


print(cntr(b, x) - cntr(a - 1, x) if a != 0 else cntr(b, x) - cntr(-1, x))
