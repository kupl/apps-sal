import sys


def main():
    l1, r1, l2, r2, k = [int(i) for i in sys.stdin.readline().strip().split()]
    l = max(l1, l2)
    r = min(r1, r2)
    if l <= r:
        print(r - l + 1 - (1 if l <= k <= r else 0))
    else:
        print(0)


def __starting_point():
    main()


__starting_point()
