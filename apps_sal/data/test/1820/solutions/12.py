import sys 
import math
from collections import Counter,defaultdict
input = sys.stdin.readline
LI=lambda:list(map(int,input().split()))
MAP=lambda:list(map(int,input().split()))
IN=lambda:int(input())
S=lambda:input()

def case():
    n=IN()
    a=LI()
    if a[0]+a[1]>a[-1]:
        print(-1)
    else:
        print(1,2,n)
for _ in range(IN()):
    case()


