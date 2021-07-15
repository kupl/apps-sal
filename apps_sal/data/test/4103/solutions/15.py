n,b,a=map(int,input().split())
l1=list(map(int,input().split()))
maxa=a
dist=0
x=0
while ( b!=0 or a!=0 ) and dist<n:
    if a==maxa:
        a-=1
        x+=1
        dist+=1
    elif l1[x]==0:
        if a>0:
            dist+=1
            a-=1
            x+=1
        else :
            x+=1
            dist+=1
            b-=1
    else :
        if b>0:
            dist+=1
            b-=1
            a+=1
            x+=1
        else :
            dist+=1
            a-=1
            x+=1
print(dist)
