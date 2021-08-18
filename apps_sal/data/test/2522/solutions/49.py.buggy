import numpy as np
import sys
read = sys.stdin.readline
n = int(input())
a = np.fromstring(read(), dtype=np.int32, sep=' ')
b = np.fromstring(read(), dtype=np.int32, sep=' ')[::-1]

kokan = []
same = -1
for i in range(n):
    if a[i] == b[i]:
        same = a[i]
if same == -1:
    print('Yes')
    print(*b)
    return

for i in range(n):
    if a[i] != b[i] and a[i] != same and b[i] != same:
        kokan.append(i)
for i in range(n):
    if a[i] == b[i]:
        if len(kokan) == 0:
            print('No')
            return
        else:
            j = kokan[-1]
            b[i], b[j] = b[j], b[i]
            kokan.pop()
print('Yes')
print(*b)
