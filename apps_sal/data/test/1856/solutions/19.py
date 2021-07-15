from collections import *
from functools import reduce
import sys
input = sys.stdin.readline

def factors(n):    
    return set(reduce(list.__add__,([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

def li():return [int(i) for i in input().rstrip('\n').split(' ')]
def st():return input().rstrip('\n')
def val():return int(input())
l = []
for i in range(val()):
    l.append(st())
l.sort(key = lambda x:len(set(x)),reverse = 1)
d = {}
tot = len(l)
for i in l:
    curr = []
    do = 1
    for j in set(i):
        if j in d and do:
            tot -= 1
            do = 0
        curr.append(j)
    for j in curr:d[j] = 1
currans = tot
l.sort()
d = {}
tot = len(l)
for i in l:
    curr = []
    do = 1
    for j in set(i):
        if j in d and do:
            tot -= 1
            do = 0
        curr.append(j)
    for j in curr:d[j] = 1
print(min(currans,tot))

