def main():
    (a, b) = list(map(int, input().split()))
    ans = a + b
    if ans >= 24:
        print((24 - ans) * -1)
    else:
        print(ans)


def __starting_point():
    main()


__starting_point()
