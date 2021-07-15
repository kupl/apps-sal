n, m = list(map(int, input().split()))
KA =[list(map(int, input().split())) for _ in range(n)]

cnt = [0]*m
for ka in KA:
  for a in ka[1:]:
    cnt[a-1] += 1

ans = 0
for i in cnt:
  if i == n:
    ans += 1
print(ans)

