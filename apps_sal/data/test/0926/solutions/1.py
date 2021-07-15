def main():
    from collections import defaultdict
    d, m = defaultdict(list), 0
    for i in range(1, int(input()) + 1):
        a, b, c = sorted(map(int, input().split()))
        d[b, c].append((a, i))
    for (a, b), l in list(d.items()):
        if len(l) > 1:
            l.sort()
            c, i = l[-1]
            x, j = l[-2]
            c += x
        else:
            c, i = l[0]
            j = 0
        if a > m < c:
            m, res = a if a < c else c, (i, j)
    print(("2\n%d %d" % res) if res[1] else ("1\n%d" % res[0]))


def __starting_point():
    main()

__starting_point()
