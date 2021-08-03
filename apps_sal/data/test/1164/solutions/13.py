from decimal import *

# newstr = oldstr.replace("M", "")


def add(l):
    num = list()
    for v in l:
        if v != '.':
            num.append(v)
    num = int(''.join(num))
    if len(l) >= 3 and l[-3] == '.':
        return num
    return num * 100


def solve():
    s = input()
    res = 0
    l = list()
    for c in s:
        if c.islower():
            if len(l) > 0:
                res += add(l)
            l = list()
        else:
            l.append(c)
    if len(l) > 0:
        res += add(l)
    return res


def prt(n):
    n = str(n)
    n = n[::-1]
    first = True
    res = ""
    while len(n) > 0:
        if first:
            s = n[:2][::1] if len(n) >= 2 else n[:1] + '0'
            res += s
            res += '.'
            n = n[len(s):]
        else:
            tmp = ""
            for i in range(3):
                if len(n) == 0:
                    break
                tmp += n[0]
                n = n[1:]
            tmp += '.'
            res += tmp

        first = False

    res = res[::-1]

    if len(res) == 3:
        res = '0' + res
    else:
        if res[0] == '.':
            res = res[1:]
    if len(res) >= 3 and res[-1] == '0' and res[-2] == '0' and res[-3] == '.':
        res = res[:-3]
    return res


print(prt(solve()))
