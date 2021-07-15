n=int(input())
a=list(map(int,input().split()))
a.sort()
x=0
y=0
s=0
if n==1:
    print(a[0])
    return
for i in a:
    if i>0:
        x+=1
    if i<0:
        y+=1
    s=s+abs(i)
if x==n or y==n:
    if x==n:
        print(s-2*a[0])
    if y==n:
        print(s+2*a[n-1])
else:
    print(s)
