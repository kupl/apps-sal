d,g = map(int, input().split())
point = [list(map(int,input().split())) for i in range(d)]

point = point[::-1]

ans = float("inf")
for bit in range(1<<d):
  total=0
  cnt=0
  for i in range(d):
    if (bit>>i)&1:
      total += (100*(d-i)*point[i][0]+point[i][1])
      cnt += point[i][0]
  if total >= g:
    ans = min(ans,cnt)
    continue
  for j in range(d):
    if (bit>>j)&1 == False:
      for k in range(point[j][0]):
        total += 100*(d-j)
        cnt += 1
        if total >= g:
          ans=min(ans,cnt)
          break
      break
print(ans)
