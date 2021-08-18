import sys
import collections

N = int(input())
AN = list(map(int, input().split()))

count = collections.Counter(AN)


edge1 = 0
edge2 = 0
for c in sorted(list(count.keys()), reverse=True):
    if count[c] >= 4:
        if edge1 == 0:
            print((c * c))
            return
        else:
            print((edge1 * c))
            return
    elif count[c] >= 2:
        if edge1 == 0:
            edge1 = c
        else:
            print((edge1 * c))
            return
else:
    print((0))
