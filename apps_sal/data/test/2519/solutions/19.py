N, K = map(int, input().split())
P = list(map(int, input().split()))
P = [(1+p)/2 for p in P]
L = [0]*(N+1)
for i in range(N):
  L[i+1] = L[i]+P[i]
print(max(L[i+K]-L[i] for i in range(N-K+1)))
