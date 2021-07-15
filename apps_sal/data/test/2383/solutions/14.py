n = int(input())
a = list(map(int,input().split()))

ans = 1
cnt = 0

if ans not in a:
  print(-1)
  return
for i in a:
  if i == ans:
    ans += 1
    continue
  cnt += 1
  
print(cnt)
