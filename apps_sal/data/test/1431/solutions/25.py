N=int(input())
*A,=map(int,input().split())
D=[[1]for _ in range(N+1)]
for i in range(2,N+1):
    j=1
    while i*j<=N:
        D[i*j].append(i)
        j+=1

D=D[1:]
B=[0]*N
ans=[]
i=1
while i<=N:
    B[-i]%=2
    if B[-i]==A[-i]:
        i+=1
        continue
    else:
        ans.append(N-i+1)
        for d in D[-i]:
            B[d-1]+=1
        B[-i]%=2
    i+=1
        
M=len(ans)
ans.sort()
print(M)
print(*ans)
