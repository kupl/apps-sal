H, W = map(int, input().split())
N = int(input())
A = list(map(int, input().split()))
ans = []

for i in range(N):
  for _ in range(A[i]):
    ans.append(i+1)
  
for i in range(H):
  if i%2 == 0:
    print(*ans[i*W:(i+1)*W])
  else:
    print(*reversed(ans[i*W:(i+1)*W]))
