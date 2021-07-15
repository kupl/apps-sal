from bisect import bisect_left as bl
from bisect import bisect_right as br
from heapq import heappush,heappop,heapify
import math
from collections import *
from functools import reduce,cmp_to_key
import sys
input = sys.stdin.readline

from itertools import accumulate

M = mod = 998244353
def factors(n):return sorted(set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0))))
def inv_mod(n):return pow(n, mod - 2, mod)
 
def li():return [int(i) for i in input().rstrip('\n').split()]
def st():return input().rstrip('\n')
def val():return int(input().rstrip('\n'))
def li2():return [i for i in input().rstrip('\n')]
def li3():return [int(i) for i in input().rstrip('\n')]
 

n = val()
s = st()

pref0 = [0]
pref1 = [0]

for i in s:
    if i == '1':
        pref1.append(pref1[-1] + 1)
        pref0.append(pref0[-1])
    elif i == '0':
        pref0.append(pref0[-1] + 1)
        pref1.append(pref1[-1])
    else:
        pref1.append(pref1[-1] + 1)
        pref0.append(pref0[-1] + 1)

next0 = [-1]
next1 = [-1]


m1 =  m2 = -1
for i in range(n):
    if s[i] == '1':m2 = i
    if s[i] == '0':m1 = i

    next0.append(m1)
    next1.append(m2)


flag = 0
last = float('inf')

for x in range(1, n + 1):
    if flag:
        ans = 0
    else:
        ans = start = 0
        while start + x <= n:
            # print(start)
            if pref0[start + x] - pref0[start] == x:
                start += x
                ans += 1
            elif pref1[start + x] - pref1[start] == x:
                start += x
                ans += 1
            else:
                start = next0[start + x] if next1[start + x] > next0[start + x] else next1[start + x]
                start += 1


    if not ans:flag = 1

    print(ans,end = ' ')
