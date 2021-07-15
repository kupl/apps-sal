n=int(input())
s=str(input())
ip=list(map(int,input().split()))
q=[1 for i in range(n)]
op=[]
for i in range(n):
    if s[i]=='L':
        q[i]=-q[i]
for i in range(n-1):
    if q[i+1]-q[i]<0:
        op.append((ip[i+1]-ip[i])/abs(q[i+1]-q[i]))
if len(op)==0:
    print(-1)
else:
    print(int(min(op)))

