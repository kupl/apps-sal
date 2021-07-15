n,k=list(map(int,input().split()))
a=list(map(int,input().split()))
ind1=-1
ind2=0
for i in range(n):
    if(a[i]>k):
        if(ind1==-1):
            ind1=i
        ind2=i
if(ind1==-1):
    print(n)
else:
    print(min(n,n-(ind2-ind1+1)))
