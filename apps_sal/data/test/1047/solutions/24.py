n = int(input())
sn = str(n)
l = len(sn)


def getDecimal(n):
    return (len(str(n)) - 1)


def intAr(a):
    b = []
    for i in a:
        b.append(int(i))
    return b


def getQDNumber(number):
    inum = int(number)
    _n = intAr(number)
    n = ''
    pointer = 0
    _len = len(number)

    if inum:
        if inum >= 10:
            while 1:
                if _n[pointer] is 0:
                    n += '0'
                else:
                    _n[pointer] -= 1
                    n += '1'

                pointer += 1

                if pointer >= _len:
                    break
        else:
            n = '1'
        if inum - int(n) >= 0:
            return n + ' ' + str(getQDNumber(str(inum - int(n))))
    return ''


n = getQDNumber(sn)
print(len(n.split(' ')) - 1)
print(n)
