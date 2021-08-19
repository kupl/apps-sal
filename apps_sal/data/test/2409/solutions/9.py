for _ in range(int(input())):
    (n, k, l) = map(int, input().split())
    dd = list(map(int, input().split()))
    (t, curld, di) = (0, 0, False)
    for d in [-2 ** 30, *dd]:
        if d > l:
            break
        ld = l - d
        if d + k <= l:
            (curld, di) = (ld, False)
            continue
        if di:
            if ld >= curld + 1:
                curld += 1
            else:
                break
        else:
            curld = min(curld - 1, ld)
            if curld == 0:
                di = True
    else:
        print('Yes')
        continue
    print('No')
