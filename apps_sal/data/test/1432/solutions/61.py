N=int(input())
A=list(map(int,input().split()))
s=sum(A)
ans=[s-2*sum(A[1::2])]
for i in range(0,N-1):
    ans.append(A[i]*2-ans[-1])
print(*ans)
