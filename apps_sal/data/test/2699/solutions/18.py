import sys
import math
import bisect
from sys import stdin,stdout
from math import gcd,floor,sqrt,log
from collections import defaultdict as dd
from bisect import bisect_left as bl,bisect_right as br

sys.setrecursionlimit(100000000)

ii     =lambda: int(input())
si     =lambda: input()
jn     =lambda x,l: x.join(map(str,l))
sl     =lambda: list(map(str,input().strip()))
mi     =lambda: map(int,input().split())
mif    =lambda: map(float,input().split())
lii    =lambda: list(map(int,input().split()))

ceil   =lambda x: int(x) if(x==int(x)) else int(x)+1
ceildiv=lambda x,d: x//d if(x%d==0) else x//d+1

flush  =lambda: stdout.flush()
stdstr =lambda: stdin.readline()
stdint =lambda: int(stdin.readline())
stdpr  =lambda x: stdout.write(str(x))

mod=1000000007


#main code
n=ii()
arr=lii()
for i in range(n):
    for j in range(4):
        if j==0:
            val=1
        elif j==1:
            val=2
        elif j==2:
            val=4
        elif j==3:
            val=3
        for k in range(arr[i]):
            ans=0
            if k>0:
                ans=2**(k-1)
            if j==3:
                val+=3*ans
                
                print(val,end=' ')
            elif j==0 or j==1:
                val+=3*ans
                print(val,end=' ')
            else:
                val+=6*ans
                print(val,end=' ')
            
        print()

                
                
                
                
            
