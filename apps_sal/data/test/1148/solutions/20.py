n=int(input())
a=list(map(int,input().split()))
l=len(a)
m=min(a)
mi=[]
b=0
for i in range(l):
    if m==a[i]:
        mi.append(i)
if len(mi)>1:
    c=l-1-mi[-1]+mi[0]
    for i in range(len(mi)-1):
        b=mi[i+1]-mi[i]-1
        if b>c:
            c=b
    print(l*m+c)
else:
    print((m+1)*l-1)

