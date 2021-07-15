N, K = map(int, input().split())
A = list(map(int, input().split()))
ans = 0
tmp = 0
j = 0
for i in range(N):
  tmp += A[i]
  while tmp >= K:
    ans += N-i
    tmp -= A[j]
    j+= 1
print(ans)
