import collections


def main():
    (n, c) = list(map(int, input().split()))
    a = list(map(int, input().split()))
    r = 0
    p = -c
    for i in a:
        d = i - p
        if d > c:
            r = 0
        r += 1
        p = i
    print(r)


def __starting_point():
    main()


__starting_point()
