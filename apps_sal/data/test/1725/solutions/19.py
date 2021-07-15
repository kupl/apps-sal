def med(list):
    nonlocal n,m
    s=sorted(list)
    return s[(n*m-1)//2]
nmd=list(input().split())
n=int(nmd[0])
m=int(nmd[1])
d=int(nmd[2])
sum=0
a=[[0]*m  for _ in range(n)]
for i in range(n):
    a[i]=[int(j) for j in input().strip().split(" ")]
sum=0
w=[]
for i in range(n):
    for j in range(m):
        w.append(a[i][j])
k=med(w)
for i in range(n):
    for j in range(m):
        sum=sum+abs(a[i][j]-k)
        w.append(a[i][j])
if sum%d==0:
    print(sum//d)
else:
    print(-1)

