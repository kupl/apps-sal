from math import gcd


def lgcd(l):
    res = l[0]
    for i in range(1, len(l)):
        res = gcd(res, l[i])

    return res


n = int(input())
print((lgcd(list(map(int, input().split())))))
