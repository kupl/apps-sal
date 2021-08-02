import sys


def readint():
    return int(sys.stdin.readline())


def readints():
    return tuple(map(int, sys.stdin.readline().split()))


def readintslist(n):
    return [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]


def main():
    a, b, c, x, y = readints()

    a_pizza = [a * i for i in range(x + 1)]
    b_pizza = [b * i for i in range(y + 1)]
    ab_pizza = [2 * c * i for i in range(max(x, y) + 1)]

    ans = []
    for i in range(max(x, y) + 1):
        ans.append(a_pizza[max(x - i, 0)] + b_pizza[max(y - i, 0)] + ab_pizza[i])
    print(min(ans))


def __starting_point():
    main()


__starting_point()
