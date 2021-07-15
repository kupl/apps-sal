a,b,k=map(int,input().split())
if a<k:
    b-=k-a
    a=0
    if b<0:
        b=0
else:
    if a-k>0:
        a-=k
    else:
        a=0
print(a,b)
