def main():
    _, t, *L = list(map(int, open(0).read().split()))
    d = [0] * t
    cand = 0
    for w, v in sorted((x, y) for x, y in zip(*[iter(L)] * 2)):
        if cand < d[-1] + v:
            cand = d[-1] + v
        for i in range(t - 1, w - 1, -1):
            if d[i - w] + v > d[i]:
                d[i] = d[i - w] + v
    print((max(cand, max(d))))


def __starting_point():
    main()


__starting_point()
