n = int(input())
hlst = list(map(int, input().split()))
bef = -1
ans = 0
cnt = 0
for h in hlst:
  if h <= bef:
    cnt += 1
    ans = max(ans, cnt)
  else:
    cnt = 0
  bef = h
print(ans)
