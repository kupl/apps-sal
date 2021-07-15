from math import*
from random import*

n = int(input())
flag = False
A, B = 0, 0
for i in range(n):
    a, b = list(map(int, input().split()))
    if a % 2 != b % 2:
        flag = True
    A, B = A + a, B + b
if A % 2 == 0 and B % 2 == 0:
    print(0)
elif A % 2 == 1 and B % 2 == 1 and flag:
    print(1)
else:
    print(-1)
