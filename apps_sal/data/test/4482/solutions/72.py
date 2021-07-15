N=int(input())
*A,=map(int,input().split())

mx=max(A)
mn=min(A)

ans=float('inf')
for i in range(mn,mx+1):
    ans=min(ans, sum([(k-i)**2 for k in A]))
print(ans)
