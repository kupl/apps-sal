N,M=list(map(int,input().split()))
A=dict()
ans=0
A=[list(map(int,input().split()))for i in range(N)]
A.sort()
for i in range(N):
    if M>A[i][1]:
        M-=A[i][1]
        ans+=A[i][0]*A[i][1]
    else:
        ans+=A[i][0]*M
        break
print(ans)

