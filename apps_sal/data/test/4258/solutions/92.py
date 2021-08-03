def main():
    a, b, t = list(map(int, input().split()))
    ans = t // a * b
    print(ans)


def __starting_point():
    main()


__starting_point()
