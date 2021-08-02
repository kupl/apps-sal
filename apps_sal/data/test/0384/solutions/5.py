import sys
import math
n = int(input())
z = input()
z += 'W'
ans = []
prev = 'W'
ctr = 0
for i in z:
    if i == 'B':
        if prev == 'W':
            ctr = 1
        else:
            ctr += 1
    else:
        if prev == 'B':
            ans.append(ctr)
    prev = i
print(len(ans))
print(*ans)
