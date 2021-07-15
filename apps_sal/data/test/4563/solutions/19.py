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

    #a,b,c=map(int, readline().rstrip().split())
    #arr=list(map(int, readline().rstrip().split()))
    n=int(readline())
    for i in range(n):
        x,y=list(map(int, readline().rstrip().split()))
        if i==0:
            a,b=x,y
            continue
        start=max(a//x,b//y)
        zz=start-1
        for z in range(start,start+1000):
            if x*z>=a and y*z>=b:
                zz=z
                break
        a,b=x*z,y*z
    print((a+b))
    #ss=readline().rstrip()
    #yn(1)

    return

if 'doTest' not in globals():
    resolve()
    return

### ----------------
### ここまで 
### ----------------

