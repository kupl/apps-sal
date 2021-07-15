q=int(input())
w=list(map(int,input().split()))
e=0
r=0
t=0
for i in w:
    if i<0:
        e+=-1-i
        r+=1
    elif i>0:
        e+=i-1
    else:
        e+=1
        t+=1
if r%2==1:
    if t>0:
        print(e)
    else:
        print(e+2)
else:
    print(e)
