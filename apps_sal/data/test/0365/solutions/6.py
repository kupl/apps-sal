n,x=list(map(int,input().split()))
a=list(map(int,input().split()))
sum1=sum(a)


if((x-sum1)==n-1):
    print("YES")
else:
    print("NO")



