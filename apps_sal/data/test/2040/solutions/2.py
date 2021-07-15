__author__ = 'PrimuS'

n = int(input())
b = [0] * n
for i in range(n):
    b[i] = int(input())

last = 0

import math


def build_smallest(csum, length):
    if math.ceil(csum / 9) == length:
        f = csum % 9
        if f == 0:
            f = 9
        return int(str(f) + "9" * (length-1))

    csum -= 1
    s = ""
    while csum > 0:
        s = str(min(csum, 9)) + s
        csum -= min(csum, 9)

    return int("1" + "0" * (length - 1 - len(s)) + s)


def build_greater(csum, x):
    x = [int(y) for y in x]

    last_possible = -1
    i = len(x) - 1
    while i >= 0:
        if x[i] < 9:
            last_possible = i
            break
        i -= 1

    if last_possible == -1:
        return 0

    if x[0] >= csum:
        return 0

    last_avail = -1
    ac_sum = 0
    for i in range(len(x)):
        ac_sum += x[i]
        if ac_sum >= csum:
            last_avail = i - 1
            break

    if last_avail == -1:
        last_avail = len(x) - 1

    pos = last_avail

    while pos >= 0:
        if x[pos] < 9:
            break
        pos -= 1

    if pos == -1:
        return 0

    res = list(x)

    res[pos] += 1
    for i in range(pos+1):
        csum -= res[i]

    i = len(res) - 1

    while i > pos:
        res[i] = min(9, csum)
        csum -= res[i]
        i -= 1

    if csum > 0:
        i = len(res) - 1
        while i >= 0:
            if res[i] < 9:
                u = min(csum, 9 - res[i])
                res[i] = res[i] + u
                csum -= u
            i -= 1
        if csum > 0:
            return 0

    res2 = 0
    for y in res:
        res2 = res2 * 10 + y

    return res2


for i in range(n):
    bx = b[i]
    cur = bx % 9
    bx -= cur
    while bx > 0:
        cur = cur * 10 + 9
        bx -= 9
    if cur <= last:
        cur = build_greater(b[i], str(last))
        if cur <= last:
            cur = build_smallest(b[i], len(str(last)) + 1)


    print(cur)
    last = cur

