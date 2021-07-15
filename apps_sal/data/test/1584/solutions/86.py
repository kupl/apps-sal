import bisect
N=int(input())
L=list(map(int,input().split()))
L=sorted(L)
ans=0
for i in range(N):
    for j in range(i+1,N):
        k=bisect.bisect_left(L,L[i]+L[j])
        ans+=k-j-1
print(ans)
