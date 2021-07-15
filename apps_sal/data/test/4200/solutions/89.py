N,M = map(int, input().split())
vote = list(map(int, input().split()))
sum = 0
for i in range(N):
  sum += vote[i]
check = sum / (4*M)
cnt = 0
for j in range(N):
  if vote[j] >= check:
    cnt += 1
if cnt >= M:
  print('Yes')
else:
  print('No')
