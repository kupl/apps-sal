def main():
    (n, z, w) = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0
    if n == 1:
        ans = abs(w - a[0])
    else:
        ans = max(abs(a[-1] - w), abs(a[-2] - a[-1]))
    print(ans)


def __starting_point():
    main()


__starting_point()
