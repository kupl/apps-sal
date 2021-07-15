import sys
# from collections import defaultdict
# t=1
t=int(input())
for i in range(t):
    # n=int(input())
    # n,m=list(map(int,sys.stdin.readline().strip().split()))
    # a,b,c,d=list(sys.stdin.readline().strip().split())
    n,k=list(map(int,sys.stdin.readline().strip().split()))
    # if(n*(a+b)>=(c-d) and n*(a-b)<=(c+d)):
    #     print("YES")
    # else:
    #     print("NO")
    
    a=list(map(int,sys.stdin.readline().strip().split()))
    x=[0]*n
    for j in range(1,n-1):
        if(a[j]>a[j-1] and a[j]>a[j+1]):
            x[j]=1
    # print(a)
    # print(x)
    k=k-2
    op=0
    curr=0
    curr=sum(x[:k])
    # print(x)
    # print(curr)
    op=curr
    op1=1

    for j in range(k,n):
        # op=max(op,curr)
        curr=curr+x[j]-x[j-k]
        if(curr>op):
            # print("here")
            op1=j-k+1
            op=curr
        # op=max(op,curr)
    op=max(op,curr)
    print(op+1,op1)
