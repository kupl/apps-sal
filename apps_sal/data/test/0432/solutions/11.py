def main():
    n, r = int(input()) + 1, 0
    cc = [0, *list(map(int, input().split()))]
    aa = [0, *list(map(int, input().split()))]
    avail = [True] * n
    for i, a in enumerate(avail):
        if a:
            j = i
            while avail[j]:
                avail[j] = False
                j = aa[j]
            c, j = cc[j], aa[j]
            if c:
                while cc[j]:
                    if c > cc[j]:
                        c = cc[j]
                    cc[j] = 0
                    j = aa[j]
                r += c
            while cc[i]:
                cc[i] = 0
                i = aa[i]
    print(r)


def __starting_point():
    main()


__starting_point()
