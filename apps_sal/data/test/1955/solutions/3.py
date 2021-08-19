def main():
    (n, m) = list(map(int, input().split()))
    dd = list(map(int, input().split()))
    aa = [0, *list(map(int, input().split()))]
    l = [True] * (m + 1)
    (l[0], total) = (False, sum(aa) + len(aa) - 2)
    for (i, e) in enumerate(dd, 1):
        if l[e]:
            if i > aa[e]:
                m -= 1
                l[e] = False
        if not m and i > total:
            print(i)
            break
    else:
        print(-1)


def __starting_point():
    main()


__starting_point()
