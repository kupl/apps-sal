import math as mt 
import sys,string,bisect
input=sys.stdin.readline
from collections import deque,defaultdict
L=lambda : list(map(int,input().split()))
Ls=lambda : list(input().split())
M=lambda : list(map(int,input().split()))
I=lambda :int(input())
n=I()
if(n%4==0):
    print(1,"A")
if(n%4==1):
    print(0,"A")
if(n%4==2):
    print(1,"B")
if(n%4==3):
    print(2,"A")

