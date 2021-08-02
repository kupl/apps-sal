import sys


def main():
    [r0, x0, y0, x1, y1] = list(map(int, sys.stdin.readline().split()))
    distance2 = (x1 - x0) * (x1 - x0) + (y1 - y0) * (y1 - y0)

    r = 2 * r0

    n = int((distance2 ** 0.5) / r) + 1

    if (n * r)**2 == distance2:
        print(n)
        return

    if ((n - 1) * r)**2 == distance2:
        print(n - 1)
        return

    if ((n + 1) * r)**2 == distance2:
        print(n + 1)
        return

    print(n)


main()
