n=int(input())
l=list(map(int,input().split()))
m=min(l)
ma=max(l)
print((2*n-1))
if m<0 and abs(m)>abs(ma):
    idx=l.index(m)+1
    for i in range(1,n+1):
        print((idx,i))
    for i in range(n-1,0,-1):
        print((i+1,i))
else:
    idx=l.index(ma)+1
    for i in range(1,n+1):
        print((idx,i))
    for i in range(2,n+1):
        print((i-1,i))
        


