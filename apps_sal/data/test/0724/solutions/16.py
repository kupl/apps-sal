n,d=list(map(int,input().split(' ')))
a=list(map(int,input().split(' ')))
c=0
t=0
l=[]
a.sort()
for i in range(0,n):
    t=0
    for j in range(i,n):
        x=a[j]-a[i]
        if x<=d:
            t+=1
    l.append(t)
print(n-max(l))

