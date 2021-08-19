import sys
import math
(n, m) = list(map(int, input().split()))
for i in range(n - 1):
    input()
w = input()
w += '.'
anc = 0
now = 1
for i in w:
    if i == 'B':
        if now:
            now = 0
            anc += 1
        else:
            continue
    else:
        now = 1
print(anc)
