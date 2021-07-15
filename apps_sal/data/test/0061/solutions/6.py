import sys
a, b = [int(x) for x in input().split()]
base = b ** (a - 1)
res1 = 0
arr = [int(x) for x in input().split()]
for digit in arr:
    res1 += digit * base
    base //= b

a, b = [int(x) for x in input().split()]
base = b ** (a - 1)
res2 = 0
arr = [int(x) for x in input().split()]
for digit in arr:
    res2 += digit * base
    base //= b

if res1 > res2:
    print('>')
elif res1 < res2:
    print('<')
else:
    print('=')


