import collections
import sys
a = input()
b = []

for i in a:
    b.append(i)

b.sort()
c = collections.Counter(b)
c = list(c.values())

for i in range(len(c)):
    if int(c[i]) % 2 == 0:
        q = 0
    else:
        q = 1
        print('No')
        return

print('Yes')
