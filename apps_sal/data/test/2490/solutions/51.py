def main():
    N = "0" + input()
    N = list(map(int, N[::-1]))
    ans = 0
    up = 0
    for i, n in enumerate(N):
        d = n + up
        if d > 5 or (i < len(N) - 1 and d == 5 and N[i + 1] >= 5):
            ans += 10 - d
            up = 1
        else:
            ans += d
            up = 0
    print(ans)


def __starting_point():
    main()


__starting_point()
