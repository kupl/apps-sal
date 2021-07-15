from math import sqrt
from itertools import accumulate


def common_divisors(x):
    ret = []
    for i in range(1, int(sqrt(x)) + 1):
        if x % i == 0:
            ret.append(i)
            ret.append(x // i)

    return ret


n, k = list(map(int, input().split()))
a = list(map(int, input().split()))

sm = sum(a)
cd = common_divisors(sm)

ans = 0
for ecd in cd:
    r = [e % ecd for e in a]
    r.sort()
    sub = [0] + list(accumulate(r))
    add = [0] + list(accumulate(ecd - e for e in r[::-1]))
    add = add[::-1]
    for sb, ad in zip(sub, add):
        if sb == ad and sb <= k:
            ans = max(ans, ecd)

print(ans)

