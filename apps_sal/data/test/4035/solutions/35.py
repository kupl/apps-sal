import math
import sys
A, B = list(map(int, input().split()))

list1 = list(range(1, 1001, 1))

s = 0
for i in list1:
    x = i // 12.5
    y = i // 10
    if x == A and y == B:
        print((str(i)))
        s = s + 1
        return

print('-1')
