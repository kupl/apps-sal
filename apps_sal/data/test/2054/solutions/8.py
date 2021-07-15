from math import inf as inf
from math import *
from collections import *
import sys
input=sys.stdin.readline
t=int(input())
while(t):
    t-=1
    a,b=list(map(int,input().split()))
    z=(a+b)//3
    print(min(a,b,z))
        
    

