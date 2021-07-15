#in1 = '4 5 8'
#in2 = ['1 1', '1 4', '1 5', '2 3', '3 1', '3 2', '3 4', '4 4']
#in1 = '10 10 20'
#in2 = ['1 1', '1 4', '1 9', '2 5', '3 10', '4 2', '4 7', '5 9', '6 4', '6 6', '6 7', '7 1', '7 3', '7 7', '8 1', '8 5', '8 10', '9 2', '10 4', '10 9']
#in1 = '1000000000 1000000000 0'
#h, w, n = map(int, in1.split())
h, w, n = list(map(int, input().split()))

idx1 = 0
ab = [[0 for i in range(2)] for j in range(n)]

black_cnt = [0] * 10
black_cnt[0] = (h - 2) * (w - 2)

if n != 0:
    while idx1 < n:
        x = input().split()
        #x = in2[idx1].split()
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
        black_cnt[0]    -= 1

for item in black_cnt:
    print(item)

