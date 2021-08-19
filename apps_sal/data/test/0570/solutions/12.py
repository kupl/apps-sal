import sys
import math
(a, b) = list(map(int, input().split()))
for i in range(10000000):
    if i % 2 == 0:
        a -= i + 1
        if a < 0:
            print('Vladik')
            break
    else:
        b -= i + 1
        if b < 0:
            print('Valera')
            break
