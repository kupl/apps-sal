from decimal import *
getcontext().prec = 500
n = int(input())
p = sorted(map(Decimal, input().split()))


def ans(p):
    ans = Decimal(0)
    for i in range(len(p)):
        cur = Decimal(1)
        for j in range(len(p)):
            if j == i:
                cur = cur * p[j]
            else:
                cur = cur * (Decimal(1) - p[j])
        ans += cur
    return ans


print('%.100f' % max((ans(p[i:]) for i in range(n))))
