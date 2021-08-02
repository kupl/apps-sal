def main():
    N = "0" + input()
    N = list(map(int, N[::-1]))
    ans = 0
    up = 0
    for i, n in enumerate(N):
        d = n + up
        # くりあがりアリ
        if d > 5 or (i < len(N) - 1 and d == 5 and N[i + 1] >= 5):
            ans += 10 - d  # 0枚の支払い（後に回す）、10-d枚のおつり
            up = 1
        # くりあがりナシ
        else:
            ans += d  # d枚の支払い、0枚のおつり
            up = 0
    print(ans)


def __starting_point():
    main()


__starting_point()
