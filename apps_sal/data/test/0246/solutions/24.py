def cmp(x1=[], x2=[]):
    len1 = len(x1)
    len2 = len(x2)
    if len1 == len2:
        for i in range(len1):
            n1 = x1[len1 - 1 - i]
            n2 = x2[len1 - 1 - i]
            if n1 != n2:
                return n1 > n2
    else:
        return len1 > len2
    return True


def add(x1=[], x2=[]):
    if not cmp(x1, x2):
        (x1, x2) = (x2, x1)
    len1 = len(x1)
    len2 = len(x2)
    for i in range(len1 - len2):
        x2.append(0)
    res = []
    flag = 0
    for (n1, n2) in zip(x1, x2):
        m = n1 + n2 + flag
        flag = m // 10
        res.append(m % 10)
    if flag:
        res.append(flag)
    return res


def minus(x1=[], x2=[]):
    if not cmp(x1, x2):
        (x1, x2) = (x2, x1)
    len1 = len(x1)
    len2 = len(x2)
    for i in range(len1 - len2):
        x2.append(0)
    res = []
    flag = 0
    for (n1, n2) in zip(x1, x2):
        m = n1 - n2 + flag
        flag = 0 if m >= 0 else -1
        res.append((m + 10) % 10)
    while res and (not res[-1]):
        res.pop()
    return res


def div(x1=[], x2=9):
    if x2 == 10:
        return x1[1:]
    else:
        x1.reverse()
        res = []
        mod = 0
        for n in x1:
            res.append((n + mod * 10) // 9)
            mod = (n + mod * 10) % 9
    res.reverse()
    while res and (not res[-1]):
        res.pop()
    return res


def multi(x1=[], x2=9):
    x1_copy = x1.copy()
    x1.insert(0, 0)
    if x2 == 10:
        return x1
    else:
        return minus(x1, x1_copy)


def __starting_point():
    input_str = input()
    (n, s) = [a for a in input_str.split()]
    nl = list([int(a) for a in list(n)])
    sl = list([int(a) for a in list(s)])
    nl.reverse()
    sl.reverse()
    x = multi(div(add(sl.copy(), [8]), 9), 9)
    y = multi(div(add(x.copy(), [9]), 10), 10)
    sumy = list([int(a) for a in list(str(sum(y)))])
    sumy.reverse()
    while not cmp(minus(y, sumy), sl):
        y = add(y, [0, 1])
        sumy = list([int(a) for a in list(str(sum(y)))])
        sumy.reverse()
    if cmp(nl, y):
        ans = add(minus(nl, y), [1])
    else:
        ans = [0]
    ans.reverse()
    ansstr = [str(a) for a in ans]
    print(''.join(ansstr))


__starting_point()
