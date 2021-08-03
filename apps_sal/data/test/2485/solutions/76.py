def main():
    h, w, m, *BOM = list(map(int, open(0).read().split()))
    row = [0] * h
    col = [0] * w
    for i, j in zip(BOM[::2], BOM[1::2]):
        i -= 1
        j -= 1
        row[i] += 1
        col[j] += 1

    p, q = max(row), max(col)
    rr = sum(1 for i in range(h) if row[i] == p)
    rl = sum(1 for i in range(w) if col[i] == q)

    cnd = rr * rl

    for i, j in zip(BOM[::2], BOM[1::2]):
        i -= 1
        j -= 1
        if (row[i], col[j]) == (p, q):
            cnd -= 1

    if cnd > 0:
        ans = p + q
    else:
        ans = p + q - 1

    print(ans)


def __starting_point():
    main()


__starting_point()
