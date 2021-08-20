import sys


def main():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    f = int(input())
    ans = 0
    if e > f:
        ans = e * min(a, d)
        x = min(a, d)
        a -= x
        d -= x
        ans += f * min(b, c, d)
        print(ans)
    else:
        ans += f * min(b, c, d)
        x = min(b, c, d)
        b -= x
        c -= x
        d -= x
        ans += e * min(a, d)
        print(ans)


def get_array():
    return list(map(int, sys.stdin.readline().split()))


def get_ints():
    return list(map(int, sys.stdin.readline().split()))


def input():
    return sys.stdin.readline().strip()


def __starting_point():
    main()


__starting_point()
