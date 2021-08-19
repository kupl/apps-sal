for _ in range(int(input())):
    (n, k, l) = list(map(int, input().split()))
    dd = list(map(int, input().split()))
    t = 0
    curld = 0
    di = False
    for d in [-2 ** 30, *dd]:
        if d > l:
            break
        ld = l - d
        if d + k <= l:
            curld = ld
            di = False
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
