### ----------------
### ここから
### ----------------

import sys
from io import StringIO
import unittest
import bisect

def bin_search(arr,ls,c):
    l=ls-1
    r = len(arr)
    while (r-l) > 1:
        m = l + (r-l)//2
        if arr[m] >= c:
            r = m
        else:
            l = m
    return l-ls+1

def resolve():
    readline=sys.stdin.readline
    n=int(readline())
    arr=list(map(int, readline().rstrip().split()))
    arr.sort()
    ans=0
    for i in range(n-2):
        for j in range(i+1,n-1):
            c = arr[i] + arr[j]
            ans += (bisect.bisect_left(arr,c,j+1) - j - 1)
            #ans += bin_search(arr,j+1,c)
    print(ans)
    return

if 'doTest' not in globals():
    resolve()
    return

### ----------------
### ここまで 
### ----------------

