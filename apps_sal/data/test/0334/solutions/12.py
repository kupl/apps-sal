a,b=list(map(int,input().split()))
s=0
c,d=list(map(int,input().split()))
flag=0
while(d!=b):
    if(s==100000):
        print(-1)
        b=d
        flag=1
    if(d<b):
        d+=max(c*((b-d)//c),c)
    else:
        b+=max(a*((d-b)//a),a)
    s+=1
if(flag==0):
    print(b)

