m, s = [int(x) for x in input().split()]

mindsum = 1
maxdsum = 9 * m

if (m == 1 and s == 0):
    print(0, 0)

elif s < mindsum or s > maxdsum:
    print(-1, -1)
else:
    mncount = s // 9
    mrest = s % 9
    if mncount == m:
        mnum = '9' * m
    elif mncount == m - 1:
        if mrest == 0:
            mnum = '1' + '8' + '9' * (mncount - 1)
        else:
            mnum = str(mrest) + '9' * mncount
    else:
        if mrest == 0:
            zerocount = m - 2 - mncount + 1
            mnum = '1' + '0' * zerocount + '8' + '9' * (mncount - 1)
        elif mrest == 1:
            zerocount = m - 1 - mncount
            mnum = '1' + '0' * zerocount + '9' * mncount
        else:
            zerocount = m - 2 - mncount
            mnum = '1' + '0' * zerocount + str(mrest - 1) + '9' * mncount

    maxnum = ''
    t = s
    while (t >= 9):
        maxnum += '9'
        t -= 9
    if (mncount != m):
        maxnum += str(t)
        while (len(maxnum) != m):
            maxnum += '0'
    print(mnum, maxnum)
