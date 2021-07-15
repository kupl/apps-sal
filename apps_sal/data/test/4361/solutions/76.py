N,K = map(int, input().split())
h = []
for i in range(N):
  tmp = int(input())
  h.append(tmp)
h.sort()

ans = h[N-1]
for i in range(0, N-K+1):
  tmp = h[i+K-1] - h[i]
  ans = min(ans, tmp)
print(ans)
