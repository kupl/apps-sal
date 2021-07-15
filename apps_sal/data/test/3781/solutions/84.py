# -*- coding: utf-8 -*-
import sys
sys.setrecursionlimit(10**9)
INF=10**18
MOD=10**9+7
input=lambda: sys.stdin.readline().rstrip()
YesNo=lambda b: bool([print('Yes')] if b else print('No'))
YESNO=lambda b: bool([print('YES')] if b else print('NO'))
int1=lambda x:int(x)-1
from collections import Counter

T=int(input())
for _ in range(T):
    N=int(input())
    a=tuple(map(int,input().split()))
    if N%2:
        print('Second')
        continue
    c=Counter(a)
    for v in c.values():
        if v%2:
            print('First')
            break
    else:
        print('Second')
