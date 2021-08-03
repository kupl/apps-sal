N = int(input())

INF = 10 ** 9


def base(x, y):
    ret = 0
    while x >= y:
        ret += x % y
        x //= y
    ret += x
    return ret


def main():
    ans = INF
    for i in range(N + 1):
        v = base(i, 6) + base(N - i, 9)
        ans = min(ans, v)
    print(ans)


def __starting_point():
    main()


__starting_point()
