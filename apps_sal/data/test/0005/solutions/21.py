# B

import math

n, pos, l, r = list(map(int, input().split()))

if l == 1 and r == n:
    print(0)
elif l == 1:
    print(int(math.fabs(r - pos) + 1))
elif r == n:
    print(int(math.fabs(l - pos) + 1))
else:
    if pos <= l:
        print(r - pos + 2)
    elif r <= pos:
        print(pos - l + 2)
    else:
        print(min(pos + r - 2*l, 2*r - l - pos) + 2)

