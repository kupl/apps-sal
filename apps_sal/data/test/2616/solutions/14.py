from math import *
t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    for i in range(n):
        if a[i]!=1:
            k=i
            break
    else:
        k=n-1
    if k%2!=0:
        print('Second')
    else:
        print('First')

