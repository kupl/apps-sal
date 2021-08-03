#from random import random, randint
from sys import stdout, stdin
import math

#n, k = map(int, input().split())
n = int(input())
s = input()

zuor = {'(': 1, ')': -1}
arr = [zuor[c] for c in s]
obpos = [z == 1 for z in arr]

suma, sume = [], []
akt = 0
for z in arr:
    akt += z
    suma.append(akt)
akt = 0
for z in reversed(arr):
    akt -= z
    sume.append(akt)
sume = list(reversed(sume))

summe = sum(arr)

if min(suma) < -2 or min(sume) < -2:
    print(0)
elif summe == 2:
    if min(suma) < 0:
        print(0)
    else:
        letzte1 = len(suma) - 1 - suma[::-1].index(1)
        ok = [i > letzte1 for i in range(n)]
        print(sum((b1 and b2 for b1, b2 in zip(ok, obpos))))
elif summe == -2:
    if min(sume) < 0:
        print(0)
    else:
        erste1 = sume.index(1)
        ok = [i < erste1 for i in range(n)]
        print(sum((b1 and not b2 for b1, b2 in zip(ok, obpos))))
else:
    print(0)
