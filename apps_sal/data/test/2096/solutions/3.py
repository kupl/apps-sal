from math import *
from random import *
n = int(input()) * 2
A = list(map(int, input().split()))
amount = [0] * 101
B = []
for i in range(n):
    if amount[A[i]] < 2:
        amount[A[i]] += 1
        B += [(A[i], i)]
B.sort()
(x, y) = ([], [])
for i in range(len(B)):
    if i % 2 == 0:
        x.append(B[i][1])
    else:
        y.append(B[i][1])
lolka = 0
aaa = 0
print(len(x) * len(y))
for i in range(n):
    if i in x:
        lolka += 1
        aaa += 1
        print(1, end=' ')
    elif i in y:
        print(2, end=' ')
    elif len(x) - lolka + aaa < n // 2:
        print(1, end=' ')
        aaa += 1
    else:
        print(2, end=' ')
print()
