import sys


def getMaxJuries(juries, m, d, t, months):
    year = 1
    res = 0
    while (t > 0):
        if (d < 0):
            m -= 1
            if(m < 0):
                m += 12
                year = 0
            d = months[m] - 1
        res = max(res, juries[year][m][d])
        d -= 1
        t -= 1

    return res


def setJury(juries, m, d, t, months, p):
    year = 1
    while (t > 0):
        if (d < 0):
            m -= 1
            if(m < 0):
                m += 12
                year = 0
            d = months[m] - 1
        juries[year][m][d] += p
        d -= 1
        t -= 1


def __starting_point():
    sys.stdin = open('input.txt', 'r')
    sys.stdout = open('output.txt', 'w')
    months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    n = int(input())
    juriesNumber = 0
    juries = [[[0 for i in range(31)] for j in range(12)] for _ in range(2)]

    for i in range(n):
        m, d, p, t = [int(x) for x in input().split()]
        m -= 1
        d -= 2
        maxJuries = getMaxJuries(juries, m, d, t, months)

        if (maxJuries + p > juriesNumber):
            juriesNumber += ((maxJuries + p) - juriesNumber)

        setJury(juries, m, d, t, months, p)

    print(juriesNumber)


__starting_point()
