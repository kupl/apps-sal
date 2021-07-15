n=int(input())
ans=0
a,b=0,0
mina,maxb=list(map(int,input().split()))
for i in range(1,n):
    a,b=list(map(int,input().split()))
    if a<mina:
        mina=a
        ans=-1
    if b>maxb:
        maxb=b
        ans=-1
    if a==mina and b==maxb:
        ans=i
if ans==-1:
    print(ans)
else:
    print(ans+1)

    

