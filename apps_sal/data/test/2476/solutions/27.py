import sys
input = sys.stdin.readline

N=int(input())
A=list(map(int,input().split()))

from collections import Counter
from itertools import accumulate
import bisect

C=Counter(A)

LIST=sorted(C.values())
LEN=len(LIST)
SUM=[0]+list(accumulate(LIST))
MIN=0
MAX=SUM[-1]

for k in range(1,N+1):
    MIN=0
    while MIN!=MAX:
        mid=(MIN+MAX+1)//2
        x=bisect.bisect_right(LIST,mid)

        if SUM[x]+(LEN-x)*mid>=mid*k:
            MIN=mid
        else:
            MAX=mid-1

    print(MIN)

