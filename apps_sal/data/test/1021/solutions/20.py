import os
import sys
from collections import deque
import pdb
import heapq
from heapq import *
from pprint import pprint
from bisect import *
if(os.getcwd() == 'C:\\Users\\User\\Desktop\\python\\Prog'):
    sys.stdin = open('input.txt', 'r')
    sys.stdout = open('output.txt', 'w')
# print(os.getcwd())


def rI():
    return [int(i) for i in input().split()]


n = rI()[0]
c = rI()
t = rI()


def rec(c):
    for i in range(1, len(c)):
        print(c[i] - c[i - 1], end=' ')
    print()


rt = []
rc = []
for i in range(1, len(c)):
    rc.append(c[i] - c[i - 1])
    rt.append(t[i] - t[i - 1])


rt.sort()
rc.sort()

if(rt == rc and c[0] == t[0]):
    print('Yes')
else:
    print('No')
