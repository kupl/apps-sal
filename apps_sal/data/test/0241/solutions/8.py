n,m,minn,maxx=list(map(int,input().split()))

L=list(map(int,input().split()))

r=0
if(minn not in L):
    L+=[minn]
    r+=1
if(maxx not in L):
    L+=[maxx]
    r+=1
valid=True

for i in range(m):
    if(L[i]<minn):
        valid=False
    if(L[i]>maxx):
        valid=False
if(r>n-m or not valid):
    print("Incorrect")
else:
    print("Correct")

