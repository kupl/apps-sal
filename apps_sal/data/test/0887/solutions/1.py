import sys
import math
n = int(input())
z = list(map(int, input().split()))
a = z.count(1)
if n == 1:
    if a != 1:
        print('NO')
    else:
        print('YES')
elif a != n - 1:
    print('NO')
else:
    print('YES')
