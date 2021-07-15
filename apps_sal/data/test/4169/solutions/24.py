N, M = list(map(int,input().split()))
AB = [list(map(int,input().split()))for _ in range(N)]

AB.sort()
cost = 0
cnt = 0
i = 0
while(cnt<M):
  a, b = AB[i]
  if M-cnt<=b:
    cost += a * (M-cnt)
    cnt = M
    break
  cost += a * b
  cnt += b
  i += 1
ans = cost
print(ans)
