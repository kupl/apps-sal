import math
import sys
n = input()
n = int(n)
a = input()
count = 0
mcount = 0
for i in range(n):
    if a[i] == '<':
        count += 1
    else:
        break
for i in range(n - 1, -1, -1):
    if a[i] == '>':
        count += 1
    else:
        break
print(count)
