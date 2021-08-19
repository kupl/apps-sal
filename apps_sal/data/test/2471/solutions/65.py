(h, w, n) = list(map(int, input().split()))
idx1 = 0
ab = [[0 for i in range(2)] for j in range(n)]
black_cnt = [0] * 10
black_cnt[0] = (h - 2) * (w - 2)
if n != 0:
    while idx1 < n:
        x = input().split()
        ab[idx1] = [int(x[0]), int(x[1])]
        idx1 += 1
    myDict = {}
    for abitem in ab:
        if abitem[0] < 3:
            sr = 0
        else:
            sr = abitem[0] - 3
        if abitem[0] > h - 3:
            lr = h - 2
        else:
            lr = abitem[0]
        if abitem[1] < 3:
            sc = 0
        else:
            sc = abitem[1] - 3
        if abitem[1] > w - 3:
            lc = w - 2
        else:
            lc = abitem[1]
        for nowRow in range(sr, lr):
            for nowCol in range(sc, lc):
                key = str(nowRow) + ',' + str(nowCol)
                if key in myDict:
                    myDict[key] += 1
                else:
                    myDict[key] = 1
    for bcnt in list(myDict.values()):
        black_cnt[bcnt] += 1
        black_cnt[0] -= 1
for item in black_cnt:
    print(item)
