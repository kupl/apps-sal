import math,sys
from collections import Counter, defaultdict, deque
from sys import stdin, stdout
input = stdin.readline
li = lambda:list(map(int,input().split()))

def case():
    n=int(input())
    a=li()
    c=0
    for i in a:
        if(i%2==0):
            c+=1
    if(c==0 or c==n):
        print("YES")
    else:
        print("NO")

for _ in range(int(input())):
    case()
