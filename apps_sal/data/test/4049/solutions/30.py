n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
acopy=a.copy()
bcopy=b.copy()
ans=[]
p=0
for i in range(3):
    p=max(p,a[i]-b[i]-b[i-1])
ans.append(str(p))
acopy=a.copy()
bcopy=b.copy()
p=0
for i in range(3):
    t=min(acopy[i-1],bcopy[i])
    p+=t
ans.append(str(p))
print(' '.join(ans))
