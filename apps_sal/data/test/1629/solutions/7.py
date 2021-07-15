n,x=map(int,input().strip().split())
a=list(map(int,input().strip().split()))
m=min(a)
x-=1
pos=-1
for i in range(n):
    if a[i]==m:
        pos=i
    if i==x and pos!=-1:
        break
for i in range(n):
    a[i]-=m
    a[pos]+=m
    
if x!=pos:
    i=(pos+1)%n
    while i!=x:
        a[i]-=1
        a[pos]+=1
        i=(i+1)%n
    a[pos]+=1
    a[i]-=1
for i in a:
    print(i,end=' ')

