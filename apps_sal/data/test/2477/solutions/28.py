n,k=map(int,input().split())
a=list(map(int,input().split()))
l,r=10**9,0
while l-r>1:
    t=(l+r)//2
    if sum((i-1)//t for i in a)>k:
        r=t
    else:
        l=t
print(l)
