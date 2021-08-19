# -*- coding: utf-8 -*-

def count(val1, val2):
    digit = 1
    while val1 >= (val2 ** digit):
        digit += 1

    res = 0
    while digit != 0:
        cnt = int(val1 // val2 ** digit)
        val1 -= (val2 ** digit) * cnt
        res += cnt
        digit -= 1

    return res, val1


N = int(input())
ans = N

for i in range(0, N + 1):
    n = i
    m = N - i
    res = 0

    cnt, nn = count(n, 9)
    n = nn
    res += cnt

    cnt, mm = count(m, 6)
    m = mm
    res += cnt

    res += n + m
    ans = min(ans, res)

print(ans)
