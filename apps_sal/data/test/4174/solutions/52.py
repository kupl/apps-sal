n,x = map(int, input().split())
l = list(map(int, input().split()))

ans = 1
t = 0
for i in l:
  t += i
  if t <= x: ans += 1
  if t >= x: break
print(ans)
