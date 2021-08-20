def judge():
    count = 0
    S = input()
    T = input()
    sList = S.split()
    sList = [int(i) for i in sList]
    tList = T.split()
    n = sList[0]
    k = sList[1]
    tList = [int(i) for i in tList]
    uList = sorted(tList)
    for num in uList:
        if 2 * k >= num:
            if k < num:
                k = num
            pass
        else:
            while True:
                k = 2 * k
                count += 1
                if 2 * k >= num:
                    if k < num:
                        k = num
                    break
    print(count)


judge()
