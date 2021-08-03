import math

a, b, x = map(int, input().split())

maxv = 10**9
minv = 1


def canbuy(n):
    tmp = a * n
    count = 0
    while n >= 1:
        n /= 10
        count += 1
    tmp += b * count
    return x >= tmp


if canbuy(1):
    midv = math.ceil((maxv + minv) / 2)
    while (maxv != midv) | (minv != midv):
        if canbuy(midv):
            minv = midv
        else:
            maxv = midv - 1
        midv = math.ceil((maxv + minv) / 2)
        # print(maxv,midv,minv)

    print(midv)
else:
    print(0)
