n=int(input())
List=[0]*(n+1)
L={}
R={}
l,r=0,0
front=0
for i in range(n):
    l,r=list(map(int,input().split()))
    L.update({l:r})
    R.update({r:l})
List[2]=L[0]
i=2
while i+2<=n:
    List[i+2]=L[List[i]]
    i+=2

for k in L:
    if R.get(k)==None:
        front=k
        break
i,List[1]=1,front
while i+2<=n:
    List[i+2]=L[List[i]]
    i+=2
print(*List[1:])

