import sys
n,m,k=list(map(int,input().split()))

if(k<n):
    print(k+1,1)
    return
k-=n
x=n-(k)//(m-1)
if(x%2==0):
    y=k%(m-1)+2   
else:
    y=m-k%(m-1)
print(x,y)
    

