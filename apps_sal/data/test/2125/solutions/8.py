import sys


def __starting_point():
    n, m = list(map(int, input().split()))
    arr = sys.stdin.readlines()
    f = 0
    flgs = {}
    for c in range(m):
        cnts = [[arr[0][c], 1]]
        for r in range(1, n):
            if arr[r][c] == cnts[-1][0]:
                cnts[-1][1] += 1
            else:
                cnts.append([arr[r][c], 1])
        strt = 0
        for i in range(len(cnts) - 2):
            if cnts[i][1] >= cnts[i + 1][1] <= cnts[i + 2][1]:
                lng = cnts[i + 1][1]
                beg = strt + cnts[i][1] - cnts[i + 1][1]
                clr = (cnts[i][0], cnts[i + 1][0], cnts[i + 2][0], lng)
                k = (clr, beg)
                if k in flgs and flgs[k][-1][-1] == c - 1:
                    flgs[k][-1][-1] = c
                elif k in flgs:
                    flgs[k].append([c, c])
                else:
                    flgs[k] = [[c, c]]

            strt += cnts[i][1]

    for flg in list(flgs.values()):
        for fl in flg:
            lng = fl[1] - fl[0] + 1
            f += (lng * (lng + 1)) // 2

    print(f)


__starting_point()
