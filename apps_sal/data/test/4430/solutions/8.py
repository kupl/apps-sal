def main():
    nobj, nbox, boxsize = list(map(int, input().split()))
    obj = list(map(int, input().split()))
    box = boxsize
    curr = 0
    ans = 0
    i = nobj - 1
    while i >= 0:
        o = obj[i]
        if o <= box:
            box -= o
            ans += 1
        else:
            curr += 1
            box = boxsize
            if curr >= nbox:
                break
            continue
        i -= 1
    print(ans)


def __starting_point():
    main()


__starting_point()
