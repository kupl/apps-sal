import sys


def minp():
    return sys.stdin.readline().strip()


(n, mm, k) = list(map(int, minp().split()))
a = list(map(int, minp().split()))


def tt(x):
    m = mm - 1
    c = 0
    res = 0
    for i in reversed(a):
        if c + i > k:
            if m == 0 or i > k:
                return res
            c = i
            m -= 1
        else:
            c += i
        res += 1
    return res


print(tt(0))
