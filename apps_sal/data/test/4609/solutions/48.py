N=int(input())
A=[]
for n in range(N):
    A.append(int(input()))

A.sort()

cnt=1
ans=0
for n in range(1,N):
    if A[n]==A[n-1]:
        cnt+=1
    else:
        if cnt%2==1:
            ans+=1
        cnt=1
    if n==N-1 and cnt%2==1:
        ans+=1
print(ans)
