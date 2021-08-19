import sys
import math
for _ in range(int(input())):
    (a, b) = map(int, input().split())
    if a <= 3:
        if a >= b <= 3 or (a == 2 and b == 3):
            print('YES')
        else:
            print('NO')
    else:
        print('YES')
