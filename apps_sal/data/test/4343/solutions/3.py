import sys
import math
import queue
sys.setrecursionlimit(1000000)

n = int(input())
a = list(input())
b = list(input())
a = [ord(ai) - 97 for ai in a]
b = [ord(bi) - 97 for bi in b]

a = [a[i] for i in range(-1, -n - 1, -1)]
b = [b[i] for i in range(-1, -n - 1, -1)]
c = [-1 for i in range(n)]
carry = 0
for i in range(n):
    if i != n - 1:
        c[i] = (carry + a[i] + b[i]) % 26
    else:
        c[i] = carry + a[i] + b[i]
    carry = (carry + a[i] + b[i]) // 26
c = [c[i] for i in range(-1, -n - 1, -1)]

carry = 0
for i in range(n):
    p = (carry * 26 + c[i]) // 2
    carry = (carry * 26 + c[i]) % 2
    c[i] = p
c = [chr(c[i] + 97) for i in range(n)]
print(''.join(c))
