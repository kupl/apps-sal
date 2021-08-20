import numpy as np
' Definitions  '


def lcm(a, b):
    return a * b // math.gcd(a, b)


MOD = 10 ** 9 + 7
x = int(input())
L = [3, 5, 7]
if x in L:
    print('YES')
else:
    print('NO')
