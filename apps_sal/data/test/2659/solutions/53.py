K = int(input())
snukePairs = []
for i in range(1, 16):
    top = 1
    if i >= 12:
        top = 3
    elif i >= 4:
        top = 2
    p = pow(10, i - top)
    fill9 = p - 1
    top_num = pow(10, max(top, 1))
    check_index = len(snukePairs)
    for j in range(pow(10, top - 1), top_num):
        num = j * p + fill9
        nn = num
        s = 0
        while nn > 0:
            s += nn % 10
            nn = nn // 10
        val = num / s
        idx = len(snukePairs) - 1
        while idx >= 0:
            if snukePairs[idx][1] > val:
                del snukePairs[idx]
            idx -= 1
        snukePairs.append([num, val])
for i in range(0, K):
    print(snukePairs[i][0])
