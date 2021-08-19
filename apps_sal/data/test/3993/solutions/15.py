# from math import *
from decimal import Decimal


def ceil(n, k):
    if(n % k != 0):
        return n // k + 1
    return n // k


n, m, k = map(int, input().split())
a = list(map(int, input().split()))
i = 0
dif = 0
ans = 0
while(i < m):
    gp = ceil(a[i] - dif, k)
    while(i < m):
        if(ceil(a[i] - dif, k) == gp):
            i += 1
        else:
            dif = i
            break
    ans += 1
print(ans)
