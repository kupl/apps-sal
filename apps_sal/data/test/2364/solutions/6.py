def main():
    input()
    s, *aa = list(map(int, input().split()))
    y = s
    for a in aa:
        s = (s * 2 + y + a) % 998244353
        y = (y * 2 + a) % 998244353
    print(s)


def __starting_point():
    main()


__starting_point()
