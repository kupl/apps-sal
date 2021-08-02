# Bhargey Mehta (Sophomore)
#DA-IICT, Gandhinagar
import sys
import math
import queue
sys.setrecursionlimit(1000000)
#sys.stdin = open("input.txt", "r")

n = int(input())
a = list(map(int, input().split()))
f = {}
for ai in a:
    if ai not in f: f[ai] = 1
    else: f[ai] += 1

mx = a[0]
for k in f:
    if f[k] > f[mx]:
        mx = k
del f
for i in range(n):
    if a[i] == mx:
        mxi = i
        break

steps = []
for i in range(mxi + 1, n):
    if a[i] < mx:
        steps.append((1, i + 1, i))
    elif a[i] > mx:
        steps.append((2, i + 1, i))
for i in range(mxi - 1, -1, -1):
    if a[i] < mx:
        steps.append((1, i + 1, i + 2))
    elif a[i] > mx:
        steps.append((2, i + 1, i + 2))
print(len(steps))
for step in steps:
    print(*step)
