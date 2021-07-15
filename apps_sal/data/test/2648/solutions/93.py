n=int(input())
a=list(map(int,input().split()))
d=dict()
for i in a:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
p=0
k=0
for i in list(d.values()):
    p+=i//2
    k-=i%2-1
print((n-(p-k//2)*2))

