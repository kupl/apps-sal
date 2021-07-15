from collections import deque
import bisect

N = int(input())
table = deque()
for n in range(N):
    a = int(input())
    if n == 0:
        table.append(a)
    else:
        if a <= table[0]:
            table.appendleft(a)
        else:
            table[bisect.bisect_left(table, a)-1] = a
            
print(len(table))
