q = int(input())

for i in range(q):

    n = int(input())
    ilist = []
    for j in range(n):
        ilist.append(list(map(int, input().rstrip().split())))
        ilist[j].append(j)
    ilist.sort()

    seglist = [2] * n
    seglist[ilist[0][2]] = 1
    goodvalue = -1
    currentmax = ilist[0][1]
    for k in range(n - 1):
        if currentmax >= ilist[k + 1][0]:
            seglist[ilist[k + 1][2]] = 1
            currentmax = max([currentmax, ilist[k + 1][1]])
        if currentmax < ilist[k + 1][0]:
            break

    if sum(seglist) == n:
        print(-1)
    else:
        print(*seglist)
