n,m=list(map(int,input().split()))
a=[]

tot=0

row=[]
col=[]
n1='row'
n2='col'
for _ in range(n):
    a+=[[int(f)for f in input().split()]]
if n>m:
    a=list(map(list,list(zip(*a))))
    n,m=m,n
    n1,n2=n2,n1
for x in range(n):
    for y in range(min(a[x])):
        row+=[x+1]
    tot+=sum(a[x])
for x in range(m):
    t=a[0][x]-min(a[0])
    if t<=0:t=0
    for y in range(t):
        col+=[x+1]
t=len(row)+len(col)
if tot-m*len(row)-n*len(col)==0:
    print(t)
    for x in row:
        print(n1,x)
    for x in col:
        print(n2,x)
else:print(-1)

