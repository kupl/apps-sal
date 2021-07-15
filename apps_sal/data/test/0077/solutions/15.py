n=int(input())
a=list(map(int,input().split()))
s=0
b=0
c=0
for i in a:
    if i>0:
        s+=i
        if i%2!=0:
            if b>0:
                b=min(b,i)
            if b==0:
                b=i
    if i<0 and i%2!=0:
        if c<0:
            c=max(c,i)
        if c==0:
            c=i
if s%2!=0:
    print(s)
else:
    if (abs(c)<b or b==0) and c!=0:
        s=s+c
    else:
        s=s-b
    print(s)
