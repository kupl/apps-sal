n=int(input())
a=list(map(int,input().split()))
s=0
ch=0
for i in range(2*n):
    s+=a[i]
dl=s//n
for i in range(2*n-1):
    for j in range(i+1,2*n):
        if a[i]>a[j]:
            a[i],a[j]=a[j],a[i]
for i in range(n):
    print(a[i], dl-a[i])

