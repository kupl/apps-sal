from math import *
n = int(input())
A = input()
r = 0
b = 0
if n % 2 == 0:
    a1 = 'br' * (n // 2)
    a2 = 'rb' * (n // 2)
else:
    a1 = 'b' + 'rb' * ((n - 1) // 2)
    a2 = 'r' + 'br' * ((n - 1) // 2)
ans1 = 0
ans2 = 0
for j in range(n):
    if A[j] == 'b':
        b += 1
    else:
        r += 1

    if A[j] != a1[j]:
        ans1 += 1
    if A[j] != a2[j]:
        ans2 += 1


if ans1 == 0 or ans2 == 0:

    print(0)
else:
    r1 = n // 2
    b1 = n % 2 + n // 2
    b2 = n // 2
    r2 = n % 2 + n // 2
    min1 = 0
    min2 = 0
    if r1 > r:
        min1 += (r1 - r)
    if b1 > b:
        min1 += (b1 - b)
    if r2 > r:
        min2 += (r2 - r)
    if b2 > b:
        min2 += (b2 - b)
    print(min(ceil(min1 + (ans1 - min1) // 2), ceil(min2 + (ans2 - min2) // 2)))
