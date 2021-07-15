import math
from collections import defaultdict
ml=lambda:map(int,input().split())
ll=lambda:list(map(int,input().split()))
ii=lambda:int(input())
ip=lambda:input()

"""========main code==============="""

t=ii()
for _ in range(t):
    x=ii()
    a=ll()
    b=ll()
    one=-1
    minus=-1
    f=0
    for i in range(x):
        if(b[i]>a[i]):
            if(one==-1):
                f=1
                break
        elif (b[i]<a[i]):
            if(minus==-1):
                f=1
                break
        if(a[i]==1):
            one=1
        elif(a[i]==-1):
            minus=1
    if(f):
        print("NO")
    else:
        print("YES")
