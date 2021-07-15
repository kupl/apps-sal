N,M=map(int,input().split())
L=[(1,a) for a in map(int,input().split())]
for _ in range(M):
  L.append(tuple(map(int,input().split())))
L=sorted(L,key=lambda x: x[1],reverse=True)
ans,k=0,0
for n,a in L:
  if n+k>=N:
    ans+=a*(N-k)
    break
  else:
    ans+=a*n
    k+=n
print(ans)
