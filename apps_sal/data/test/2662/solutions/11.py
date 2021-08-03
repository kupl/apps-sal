
from bisect import bisect_left, bisect_right
from collections import deque
n = int(input())
l = []
for _ in range(n):
    a = int(input())
    l.append(a)


li = deque([l[0]])
for j in range(1, n):
    ai = l[j]
    ind = bisect_left(li, ai)
    if ind == 0:
        li.appendleft(ai)
    else:
        li[ind - 1] = ai
print((len(li)))
