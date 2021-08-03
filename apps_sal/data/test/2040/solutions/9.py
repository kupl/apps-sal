def cr_mn(sm):
    d = 1
    res = 0
    while sm > 0:
        res += min(9, sm) * d
        sm -= min(9, sm)
        d *= 10
    return res


def cr_ln(sm, ln):
    if sm == 0:
        return '0' * ln
    res = int('1' + '0' * (ln - 1))
    d = 1
    sm -= 1
    while sm > 0:
        res += min(9, sm) * d
        sm -= min(9, sm)
        d *= 10
    return str(res)


def cr_min(sm, lst):
    r1 = cr_mn(sm)
    if r1 > int(lst):
        r1 = str(r1)
        return '0' * (len(lst) - len(r1)) + str(r1)
    ln = len(lst)
    lfs = int(lst[0])
    if lfs >= sm:
        return '-1'
    if ln == 1:
        return sm
    r1 = cr_min(sm - lfs, lst[1:])
    if r1 == '-1':
        if lfs == 9:
            return '-1'
        r1 = str(cr_mn(sm - lfs - 1))
        return str(lfs + 1) + '0' * (ln - 1 - len(r1)) + r1
    return lst[0] + r1


n = int(input())
a = []
for i in range(n):
    a += [int(input())]
b = [-1 for i in range(n)]
b[0] = str(cr_mn(a[0]))
print(b[0])
for i in range(1, n):
    b[i] = cr_min(a[i], b[i - 1])
    if b[i] == '-1':
        b[i] = cr_ln(a[i], len(b[i - 1]) + 1)
    print(b[i])
