n,m=[int(x) for x in input().split()]
L=[0]*(n+1)
for i in range(m):
    l=[int(x) for x in input().split()]
    max=-1
    for i in range(n):
        if l[i]>max:
            maxval=i+1
            max=l[i]
    L[maxval]+=1
max=-1
for i in range(n+1):
    if L[i]>max:
        maxval=i
        max=L[i]
print(maxval)

