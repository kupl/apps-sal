n=int(input())
a=list(map(int,input().split()))
a1=0
t=0
for i in range(n):
    t+=a[i]
    if i%2==0:
        if t<=0:
            a1+=1-t
            t=1
    else:
        if t>=0:
            a1+=1+t
            t=-1
a2=0
t=0
for i in range(n):
    t+=a[i]
    if i%2==1:
        if t<=0:
            a2+=1-t
            t=1
    else:
        if t>=0:
            a2+=1+t
            t=-1
print(min(a1,a2))
