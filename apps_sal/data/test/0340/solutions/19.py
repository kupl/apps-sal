from math import log, ceil


def factor1(n):
    num = 2
    res = set()
    while num ** 2 <= n:
        while n % num == 0:
            res.add(num)
            n = n // num
        num += 1
    if n > 1:
        res.add(n)
    ans = 1
    for x in res:
        ans *= x
    return ans


def factor(n):
    num = 2
    res = dict()
    while num ** 2 <= n:
        while n % num == 0:
            res[num] = res.get(num, 0) + 1
            n = n // num
        num += 1
    if n > 1:
        res[n] = res.get(n, 0) + 1
    return res


n = int(input())
min_ = factor1(n)
kek = sorted(factor(n).values())
if min_ == n:
    print(n, 0)
elif kek[0] == kek[-1] and log(kek[-1], 2) // 1 == log(kek[-1], 2):
    print(min_, int(log(kek[-1], 2)))
else:
    print(min_, ceil(log(kek[-1], 2)) + 1)

