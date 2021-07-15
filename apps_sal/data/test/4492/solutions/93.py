n,x=map(int,input().split())
l=list(map(int,input().split()))
c=0
t=l[0]
for a in l[1:]:
    d=t+a-x
    if d>0:
        if a<d:
            a=0
        else:
            a-=d
        c+=d
    t=a
print(c)
