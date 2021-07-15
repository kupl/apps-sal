n,m=[int(x) for x in input().split()]
a=[int(x) for x in input().split()]
s=sum(a)
need=0
a.sort()
j=1
flag=0
k=max(a)
if n==1:
    print(0)
else:
    for i in range(n):
        if a[i]<j:
            flag=1
        else:
            flag=0
        if a[i]==1:
            need+=1
        elif a[i]>=j and i!=n-1:
            need+=1
        elif a[i]>=j and i==n-1 and j<=k:
            need+=k-j+1
        else:
            need+=1
        if flag!=1:
            j+=1
    print(s-need)
        
        

