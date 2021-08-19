def main():
    (n, m, k) = list(map(int, input().split()))
    (c, *cc) = list(map(int, input().split()))
    (pp, *ppp) = (list(map(int, input().split())) for _ in range(n))
    inf = 2 ** 47
    inf2 = inf * 2
    nxt = [[0 if i == c - 1 else inf for i in range(m)] if c else pp]
    for (c, pp) in zip(cc, ppp):
        newrow = [inf] * m
        (cur, nxt) = (nxt, [newrow])
        if c:
            c -= 1
            for row in cur:
                p = row[c]
                if newrow[c] > p:
                    newrow[c] = p
                if len(nxt) == k:
                    break
                row[c] = inf2
                newrow = [inf] * m
                newrow[c] = min(row)
                nxt.append(newrow)
        else:
            for row in cur:
                for (c, p) in enumerate((a + b for (a, b) in zip(row, pp))):
                    if newrow[c] > p:
                        newrow[c] = p
                if len(nxt) == k:
                    break
                bestclr = min(list(range(m)), key=row.__getitem__)
                (x, row[bestclr]) = (row[bestclr], inf2)
                newrow = [a + x for a in pp]
                newrow[bestclr] = min(row) + pp[bestclr]
                nxt.append(newrow)
    p = min(nxt[-1])
    print(p if p < inf else -1)


def __starting_point():
    main()


__starting_point()
