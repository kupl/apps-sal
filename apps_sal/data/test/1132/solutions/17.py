from array import array
from collections import Counter
(n, m) = list(map(int, input().split()))
a = array('L')
a.extend((0 for i in range(n)))
for i in range(m):
    (x, y) = list(map(int, input().split()))
    a[x - 1] += 1
    a[y - 1] += 1
ca = array('L')
ca.extend((0 for i in range(max(a) + 1)))
for i in a:
    ca[i] += 1


def c(i):
    if i >= len(ca) or i < 0:
        return 0
    else:
        return ca[i]


if c(1) == 2 and c(2) == n - 2:
    print('bus topology')
elif c(2) == n:
    print('ring topology')
elif c(1) == n - 1 and c(n - 1) == 1:
    print('star topology')
else:
    print('unknown topology')
