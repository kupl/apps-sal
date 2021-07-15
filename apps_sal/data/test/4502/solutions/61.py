n = int(input())
a = list(map(int, input().split()))
from collections import deque
d = deque()


if len(a) %2 == 0:
    d.extend(a[::2])
    d.extendleft(a[1::2])
else:
    d.extend(a[1::2])
    d.extendleft(a[::2])
print((*list(d)))

