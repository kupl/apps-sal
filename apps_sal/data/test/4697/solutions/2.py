def main():
    n, m = map(int, input().split())

    if m - 2 * n >= 0:
        m -= 2 * n
        ans = n
        n = 0

        if (m - 2 * n) % 4 == 0:
            tmp = (m - 2 * n) // 4
        else:
            tmp = (m - 2 * n) // 4 + 1

        ans += (m - 2 * tmp) // 2

    else:
        ans = m // 2

    print(ans)


def __starting_point():
    main()
__starting_point()
