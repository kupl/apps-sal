def main():
    q = int(input())
    for _ in range(q):
        n = int(input())
        slist = list(sorted(map(int, input().split())))
        (li, ri) = (0, 4 * n - 1)
        ans = None
        for j in range(n):
            if slist[li] != slist[li + 1] or slist[ri] != slist[ri - 1]:
                print('NO')
                break
            if ans is None:
                ans = slist[li] * slist[ri]
                li += 2
                ri -= 2
            elif ans != slist[li] * slist[ri]:
                print('NO')
                break
            else:
                li += 2
                ri -= 2
        else:
            print('YES')


def __starting_point():
    main()


__starting_point()
