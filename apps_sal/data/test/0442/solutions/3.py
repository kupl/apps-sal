import math
import sys,string,bisect,heapq
input=sys.stdin.readline
from collections import deque,defaultdict
L=lambda : list(map(int,input().split()))
Ls=lambda : list(input().split())
M=lambda : list(map(int,input().split()))
I=lambda :int(input())
n=I()
if(n%2==0 or n<=3):
    print("NO")
else:
    print(1,(n-3)//2)
    

