from math import pi


def main():
    n = int(input())
    s = sum(map(int, input().split()))
    if s % n:
        n -= 1
    print(n)


def __starting_point():
    main()
__starting_point()
