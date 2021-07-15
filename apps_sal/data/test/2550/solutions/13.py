import math,sys
from collections import Counter, defaultdict, deque
from sys import stdin, stdout
input = stdin.readline
li = lambda:list(map(int,input().split()))

def case():
    n,m=li()
    a=li()
    s=sum(a)
    print(min(s,m))

for _ in range(int(input())):
    case()
