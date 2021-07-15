def dp(n,m):
    mark = [0 for i in range(m)]
    a = list(map(int,input().split()))
    for x in a:
        for i in range(m):
            if(mark[i]==1):
                k=(i+x%m)%m
                if(mark[k]!=1):
                    mark[k]=2
        for i in range(m):
            if(mark[i]>0):
                mark[i]=1
        mark[x%m]=1
    return mark[0]
import sys
input = sys.stdin.readline
n,m = list(map(int,input().split()))
flag = True
if(n<=m):
    flag=(dp(n,m)!=0)
if(flag):
    print("YES")
else:
    print("NO")

