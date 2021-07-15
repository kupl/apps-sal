n,m,i,j,a,b=map(int,input().split())
ans=n*m+1
if (i-1)%a==0 and (m-j)%b==0:
    x=min( (i-1)//a,(m-j)//b)
    y=max( (i-1)//a,(m-j)//b)
    if (y-x)%2==0:
        if (y-x)==0 or ( ((i-a)>=1 or(i+a)<=n) and ((j+b)<=m or (j-b)>=1) ):
            ans=min(ans,x+(y-x))
if (n-i)%a==0 and (j-1)%b==0:
    x=min( (n-i)//a,(j-1)//b)
    y=max( (n-i)//a,(j-1)//b)
    if (y-x)%2==0:
        if (y-x)==0 or ( ((i-a)>=1 or(i+a)<=n) and ((j+b)<=m or (j-b)>=1) ):
            ans=min(ans,x+(y-x))
if (i-1)%a==0 and (j-1)%b==0:
    x=min( (i-1)//a,(j-1)//b)
    y=max( (i-1)//a,(j-1)//b)
    if (y-x)%2==0:
        if (y-x)==0 or ( ((i-a)>=1 or(i+a)<=n) and ((j+b)<=m or (j-b)>=1) ):
            ans=min(ans,x+(y-x))
if (n-i)%a==0 and (m-j)%b==0:
    x=min( (n-i)//a,(m-j)//b)
    y=max( (n-i)//a,(m-j)//b)
    if (y-x)%2==0 :
        if (y-x)==0 or ( ((i-a)>=1 or(i+a)<=n) and ((j+b)<=m or (j-b)>=1) ):
            ans=min(ans,x+(y-x))
if ans!=(n*m+1):
    print(ans)
else :
    print("Poor Inna and pony!")
