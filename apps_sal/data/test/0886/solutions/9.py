def ans():
    ap = list(input())
    #b= a[::-1]
    a = [int(i) for i in ap]
    ans = []
    kkk = -1
    for i in range(len(a)):
        if a[i] % 2 == 0:
            kkk = i
            if a[-1] > a[i]:
                ap[-1], ap[i] = ap[i], ap[-1]
                print("".join(ap))
                return

    if kkk != -1:
        ap[kkk], ap[-1] = ap[-1], ap[kkk]
        print("".join(ap))
        return
    print(-1)

    return


ans()
