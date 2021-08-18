def main():
    n, k = map(int, input().split())
    s = input()

    ans = 0
    x = s[0]
    for i in range(1, n):
        if x == s[i]:
            ans += 1
        else:
            x = s[i]
    print(min(ans + 2 * k, n - 1))


def __starting_point():
    main()


__starting_point()
