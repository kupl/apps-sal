import sys


def input():
    return sys.stdin.readline()[:-1]


def main():
    s = input()
    t = input()

    listS = []
    for i in range(len(s)):
        listS.append(s[i])

    listT = []
    for i in range(len(t)):
        listT.append(t[i])

    listS = sorted(listS)
    listT = sorted(listT, reverse=True)

    sortedS = ''
    for i in range(len(listS)):
        sortedS += listS[i]
    sortedT = ''
    for i in range(len(listT)):
        sortedT += listT[i]

    if sortedS < sortedT:
        print('Yes')
    else:
        print('No')


def __starting_point():
    main()


__starting_point()
