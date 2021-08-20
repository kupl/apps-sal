def main():
    (h, w) = list(map(int, input().split()))
    if h % 3 == 0 or w % 3 == 0:
        print(0)
        return
    ans = h * w
    for _ in range(2):
        i = h // 3
        j = w // 2
        x = [(i - 1, h - i + 1), (i, h - i), (i + 1, h - i - 1)]
        y = [(j - 1, w - j + 1), (j, w - j), (j + 1, w - j - 1)]
        for (u, v) in x:
            (a, b) = (v // 2, v - v // 2)
            s = [w * u, w * a, w * b]
            d = max(s) - min(s)
            ans = min(ans, d)
            for (s, t) in y:
                s = [u * w, v * s, v * t]
                d = max(s) - min(s)
                ans = min(ans, d)
        (w, h) = (h, w)
    print(ans)


def __starting_point():
    main()


__starting_point()
