'''input
5
1 5 7 8 2
'''
import sys
from collections import defaultdict as dd
from itertools import permutations as pp
from itertools import combinations as cc
from collections import Counter as ccd
from random import randint as rd
from bisect import bisect_left as bl
import heapq
mod = 10**9 + 7


def ri(flag=0):
    if flag == 0:
        return [int(i) for i in sys.stdin.readline().split()]
    else:
        return int(sys.stdin.readline())


n = ri(1)
a = ri()
even = []
odd = []

for i in a:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

even.sort(reverse=True)
odd.sort(reverse=True)

ans = 0

i = 0
j = 0
f = 0
while 1:
    try:
        if f == 0:
            f = 1
            ans += even[i]
            i += 1
        else:
            f = 0
            ans += odd[j]
            j += 1
    except:
        break

ans1 = 0

i = 0
j = 0
f = 1
while 1:
    try:
        if f == 0:
            f = 1
            ans1 += even[i]
            i += 1
        else:
            f = 0
            ans1 += odd[j]
            j += 1
    except:
        break


print(sum(a) - max(ans, ans1))
