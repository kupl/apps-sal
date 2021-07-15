import sys
n=int(sys.stdin.readline())
l=list(map(int,sys.stdin.readline().split()))
k=0
q=0
z=[0]*n
for i in range(n):
    z[l[i]-1]=i
ans=0
while k<n-1:
    ans+=abs(z[k]-z[k+1])
    k+=1
print(ans)
