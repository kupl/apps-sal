import sys
read = sys.stdin.read


def main():
    n = int(input())
    rc = tuple(input())
    rc2 = [c == 'W' for c in rc]
    r1 = sum(rc2)
    r2 = n - r1
    r3 = sum(rc2[:r2])
    print(min(r1, r2, r3))


def __starting_point():
    main()


__starting_point()
