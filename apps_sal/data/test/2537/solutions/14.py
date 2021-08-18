import math
from collections import deque, defaultdict
from sys import stdin, stdout
def listin(): return list(map(int, input().split()))
def mapin(): return map(int, input().split())


for _ in range(int(input())):
    s = input()
    t = input()
    p = input()
    cs = defaultdict(int)
    ct = defaultdict(int)
    cp = defaultdict(int)
    for i in s:
        cs[i] += 1
    for i in t:
        ct[i] += 1
    for i in p:
        cp[i] += 1
    flag = True
    for i in ct.keys():
        if ct[i] > cs[i] + cp[i]:
            flag = False
    if flag:
        i = 0
        j = 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        if i == len(s):
            print('YES')
        else:
            print('NO')
    else:
        print('NO')
