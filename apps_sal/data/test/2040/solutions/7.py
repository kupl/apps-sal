def getnum(digsum):
    if digsum < 0:
        return 0
    if digsum < 10:
        return digsum
    else:
        nnine = digsum // 9
        res = digsum % 9
        for i in range(nnine):
            res = 10 * res + 9
        return res


def digsumf(n):
    return sum([int(i) for i in str(n)])


def getnext(bnum, last):
    if last == 0:
        return getnum(bnum)

    k = last + 1
    digsum = digsumf(k)
    diff = bnum - digsum
    if diff >= 0 and 9 - k % 10 >= diff:
        return k + diff

    omitsum = 0
    startdigsum = digsumf(last)
    lastl = [int(i) for i in str(last)]
    digsum = digsumf(last)
    l = 10
    i = 1
    while True:
        if i == 1 and len(str(l)) - 1 <= len(lastl):
            omitsum += lastl[-(len(str(l)) - 1)]
        if (last // l) % 10 + i > 9:
            l *= 10
            i = 1
            continue
        k = (last // l) * l + l * i
        digsum = startdigsum - omitsum + i
        diff = bnum - digsum
        r = getnum(diff)
        if diff >= 0 and len(str(r)) <= len(str(l // 10)):
            return r + k
        if diff < 0:
            l *= 10
            i = 1
        else:
            i += 1


n = int(input())
last = 0
for i in range(n):
    last = getnext(int(input()), last)
    print(last)
