def main():
    h, w = list(map(int, input().split()))
    d = h * w
    for i in range(1, h):
        sh = (h - i) // 2
        s = (i * w, sh * w, (h - i - sh) * w)
        d = min(max(s) - min(s), d)
        sv = w // 2
        s = (i * w, (h - i) * sv, (h - i) * (w - sv))
        d = min(max(s) - min(s), d)
    for i in range(1, w):
        sv = (w - i) // 2
        s = (h * i, h * sv, h * (w - i - sv))
        d = min(max(s) - min(s), d)
        sh = h // 2
        s = (h * i, sh * (w - i), (h - sh) * (w - i))
        d = min(max(s) - min(s), d)
    print(d)


def __starting_point():
    main()


__starting_point()
