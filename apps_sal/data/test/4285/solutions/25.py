from bisect import bisect_left as bl
from bisect import bisect_right as br
from heapq import heappush,heappop,heapify
import math
from collections import *
from functools import reduce,cmp_to_key
import sys
input = sys.stdin.readline

from itertools import accumulate
from functools import lru_cache

M = mod = 10 ** 9 + 7
def factors(n):return sorted(set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0))))
def inv_mod(n):return pow(n, mod - 2, mod)
 
def li():return [int(i) for i in input().rstrip('\n').split()]
def st():return input().rstrip('\n')
def val():return int(input().rstrip('\n'))
def li2():return [i for i in input().rstrip('\n')]
def li3():return [int(i) for i in input().rstrip('\n')]



n = val()
l = list(st())





questions1 = [0]
As = [0]
Cs = [0]
questions2 = [0]

for i in range(n):

    questions1.append(questions1[-1])
    if l[i] == '?':
        questions1[-1] += 1
        
    
    As.append(As[-1])
    if l[i] == 'a':
        As[-1] += 1

for i in range(n - 1, -1, -1):
    questions2.append(questions2[-1])
    if l[i] == '?':
        questions2[-1] += 1
        
    
    Cs.append(Cs[-1])
    if l[i] == 'c':
        Cs[-1] += 1

Cs.pop()
questions2.pop()

Cs.reverse()
questions2.reverse()


ans = 0
for i in range(n):
    if l[i] == 'b' or l[i] == '?':
        left = right = 0
        left = As[i] * pow(3, questions1[i], mod) % mod
        if questions1[i]:left = (left + pow(3, questions1[i] - 1, mod) * questions1[i]) % mod
        right = Cs[i] * pow(3, questions2[i], mod) % mod
        if questions2[i]:right = (right + pow(3, questions2[i] - 1, mod) * questions2[i]) % mod

        # print(l, i, left, right)

        ans = (ans + left * right) % mod
print(ans)
