import sys
# from collections import defaultdict
# t=1
t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,sys.stdin.readline().strip().split()))
    # a,b,c,d=list(sys.stdin.readline().strip().split())
    # n,k=list(map(int,sys.stdin.readline().strip().split()))
    
    x1=[]
    x2=[]
    
    x=a[0]
    mni=0
    for j in range(n):
       if(a[j]<x):
           x=a[j]
           mni=j
       x1.append([x,mni])
    
    x=a[n-1]
    mni=n-1
    for j in range(n-1,-1,-1):
        if(a[j]<x):
            x=a[j]
            mni=j
        x2.append([x,mni])
        
    f=0
    for j in range(1,n-1):
        if(x1[j-1][0]<a[j] and a[j]>x2[n-j-1][0]):
            print("YES")
            print(x1[j-1][1]+1,j+1,x2[n-j-1][1]+1)
            f=1
            break
    if(f):
        continue
    print("NO")

