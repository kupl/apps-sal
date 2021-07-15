h,a = map(int,input().split())
ans = 0
for _ in range(h):
  h -= a
  ans += 1
  if h <= 0:
    break
print(ans)
