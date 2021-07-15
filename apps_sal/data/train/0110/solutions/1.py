from math import *
from random import *
for t in range(int(input())):
    n, k = map(int, input().split())
    mas = list(map(int, input().split()))
    pick = [0 for i in range(n)]
    for i in range(1, n - 1):
        pick[i] = pick[i - 1]
        if mas[i] > mas[i - 1] and mas[i] > mas[i + 1]:
            pick[i] += 1
    if n > 1:
        pick[n - 1] = pick[n - 2]
    mx = 0
    mxotv = 0
    for i in range(0, n - k + 1):
        if i + k - 2 < 0:
            continue
        res = pick[i + k - 2]
        res -= pick[i]
        if res > mx:
            mx = res
            mxotv = i
    print(mx + 1, mxotv + 1)
