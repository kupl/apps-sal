from bisect import bisect_left
from bisect import bisect_right
n, q = list(map(int, input().split()))
s = input()
lr = [tuple(map(int, input().split())) for _ in range(q)]

ac = []
for i in range(n-1):
    if s[i] == 'A' and s[i+1] == 'C':
        ac.append(i)

if ac == []:
    for i in range(q):
        print((0))
    return

for l, r in lr:
    l -= 1
    r -= 1
    li = bisect_left(ac, l)
    ri = bisect_right(ac, r)
    if li == ri:
        print((0))
    elif r > ac[ri-1]:
        print((ri-li))
    else:
        print((ri-li-1))

