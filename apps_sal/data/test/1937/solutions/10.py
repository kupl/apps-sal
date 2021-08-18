

import math
n = int(input())
blist = list(map(int, input().rstrip().split()))


alist = [0 for i in range(n)]


alist[0] = 0
alist[n - 1] = blist[0]

for i in range(1, n // 2):
    if blist[i] <= blist[i - 1]:
        alist[i] = alist[i - 1]
        alist[n - i - 1] = blist[i] - alist[i]
    else:
        alist[n - i - 1] = alist[n - i]
        alist[i] = blist[i] - alist[n - i - 1]


aliststr = [str(i) for i in alist]

print(" ".join(aliststr))
