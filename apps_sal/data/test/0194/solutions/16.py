n,a,b=list(map(int,input().split()))
data = list(map(int,input().split()))
h=c=0
for i in data:
    if i==1:
        if a>0:
            a-=1
        elif b>0:
            b-=1
            h+=1
        elif h>0:
            h-=1
        else:
            c+=1
    else:
        if b>0:
            b-=1
        else:
            c+=2
            
print(c)

