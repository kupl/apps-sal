N,K=map(int,input().split())
G=[1]+[0]*N
for i in range(K):
 for j in range(i,N):G[j+1]+=G[j]
print((G[-2]<<N-K-(K<N))%(10**9+7))
