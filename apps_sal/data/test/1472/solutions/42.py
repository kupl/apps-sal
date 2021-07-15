### ----------------
### ここから
### ----------------

import sys
from io import StringIO
import unittest

def yn(b):
    print(("Yes" if b==1 else "No"))
    return

def resolve():
    readline=sys.stdin.readline

    n,x,y=list(map(int, readline().rstrip().split()))
    ans = [0] * (n-1)
    for i in range(1,n+1):
        for j in range(i+1,n+1):
            d1 = abs(i-x) + abs(j-x)
            d2 = abs(i-y) + abs(j-y)
            d3 = abs(i-x) + abs(j-y) + 1
            d4 = abs(i-y) + abs(j-x) + 1
            d5 = abs(i-j)
            d=min(d1,d2,d3,d4,d5)
            ans[d-1]+=1
    for a in ans:
        print(a)
    #arr=list(map(int, readline().rstrip().split()))
    #n=int(readline())
    #ss=readline().rstrip()
    #yn(1)

    return

if 'doTest' not in globals():
    resolve()
    return

### ----------------
### ここまで 
### ----------------

