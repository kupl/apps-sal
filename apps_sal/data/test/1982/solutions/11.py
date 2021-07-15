from math import *
for zz in range(int(input())):
    n, k = list(map(int, input().split()))
    if n < k**2 or n % 2 == 1 - (k % 2):
        print('NO')
    else:
        print('YES')

