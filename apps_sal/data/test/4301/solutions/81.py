n = int(input())
alist = [int(input()) for _ in range(n)]

import copy
alist_copy = copy.copy(alist)

alist_copy.sort()
max_value = alist_copy[-1]
next_value = alist_copy[-2]
for a in alist:
    if a == max_value:
        print(next_value)
    else:
        print(max_value)
