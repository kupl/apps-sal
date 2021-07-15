s=input().split()
n=int(s[0])
k=int(s[1])
L=list(map(int,input().split()))

lx=0
while L[lx]==0:
    lx+=1
A=[]
for i in range(lx,n):
    A.append(L[i])
n=len(A)
n=len(A)
def good(l):
    coeff=1
    tot=0
    for i in reversed(list(range(n))):
        tot+=coeff*A[i]
        if tot>=k:
            return True
        coeff=(coeff*(n-i-1+l))//(n-i)
    return False
ans=0
for i in range(1,10):
    if good(i):
        ans=i
        break
if ans==0:
    l=1
    r=k
    while True:
        if l==r:
            ans=l
            break
        if l+1==r:
            if good(l):
                ans=l
            else:
                ans=r
            break
        m=(l+r)//2
        if good(m):
            r=m
        else:
            l=m+1
for i in range(n):
    if A[i]>=k:
        ans=0
print(ans)

