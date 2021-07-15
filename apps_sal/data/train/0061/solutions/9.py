from math import *
t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    for i in range(1,n-1):
        if a[i]>a[i-1] and a[i]>a[i+1]:
            print('YES')
            print(i,i+1,i+2)
            break
    else:
        print('NO')

