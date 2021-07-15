N, K = map(int, input().split())
A = list(map(int, input().split()))
L = [0]*(N+1)
for i in range(N):
  L[i+1]=L[i]+A[i]
r, cnt = 0, 0
for l in range(N):
  while r<N and L[r+1]-L[l]<K:
    r += 1
  cnt += (N-r)
print(cnt)
