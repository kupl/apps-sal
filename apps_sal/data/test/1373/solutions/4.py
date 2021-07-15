N,K=map(int,input().split())
p=10**9 + 7
ans=0
for i in range(K-1,N+1):
  L_min=i*(i+1)//2
  L_max=(N*(N+1)//2)-((N-i-1)*(N-i)//2)
  ans += (L_max-L_min+1)%p
print(ans%p)
