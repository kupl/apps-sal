import sys
a,b,c,d=list(map(int,input().split()))
s=0;p=1;i=1
while True:
    if i%2:
        s+=p*a/b
        p*=(1-a/b)
    else:
        p*=(1-c/d)
    if p<1e-7:
        print(round(s,6))
        return
    i=i+1

