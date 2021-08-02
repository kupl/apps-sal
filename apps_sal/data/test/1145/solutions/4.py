import sys


def main():
    sys.stdin.readline()
    badges = map(int, sys.stdin.readline().split())

    price = 0
    existing_badges = set()
    for b in sorted(badges):
        while b in existing_badges:
            price += 1
            b += 1
        existing_badges.add(b)

    print(price)


def __starting_point():
    main()


__starting_point()
