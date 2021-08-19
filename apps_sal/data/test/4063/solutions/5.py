def main():
    N = int(input())
    d = sorted(list(map(int, input().split())))
    ans = 0
    if d[N // 2] != d[N // 2 - 1]:
        ans = d[N // 2] - d[N // 2 - 1]
    print(ans)


def __starting_point():
    main()


__starting_point()
