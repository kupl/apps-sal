import sys


def main():
    n, t = tuple([int(y) for y in input().split()])
    a = [int(x) for x in input().split()]
    c = 1
    while True:
        c = c + a[c - 1]
        if c == t:
            print("YES")
            return
        elif c > t:
            print("NO")
            return
    print("NO")


def __starting_point():
    main()


__starting_point()
