def main():
    (h, a) = map(int, input().split(' '))
    ans = 0
    while h > 0:
        h -= a
        ans += 1
    print(ans)


def __starting_point():
    main()


__starting_point()
