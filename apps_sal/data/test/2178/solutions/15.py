n=int(input())
a=[int(s) for s in input().split()]
id=[0]*(n+1)
for i in range(n):
    id[a[i]]=i+1
b=[int(s) for s in input().split()]
max=0
for i in b:
    if id[i]>max:
        print(id[i]-max,end=' ')
        max=id[i]
    else:
        print(0,end=' ')
