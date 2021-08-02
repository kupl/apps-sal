from math import gcd
import sys
input = sys.stdin.readline

t = int(input())

for ccc in range(t):
    x = int(input())

    if x > 6 + 10 + 14:
        print('YES')
        if x - 30 not in [6, 10, 14]:
            print(6, 10, 14, x - 30)
        else:
            print(6, 10, 15, x - 31)
    else:
        print('NO')
