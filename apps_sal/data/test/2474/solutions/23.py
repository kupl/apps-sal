def main():
    n = int(input())
    c = sorted(list(map(int, input().split())))
    mod = 10 ** 9 + 7
    ans = 0
    for (i, j) in enumerate(c):
        ans = (ans + j * (n - i + 1)) % mod
    ans = ans * 4 ** (n - 1) % mod
    print(ans)


def __starting_point():
    main()


__starting_point()
