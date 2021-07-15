cur, add = 0, 1
ans = 0
n = int(input())
while cur < n:
  cur += add
  add *= 2
  ans += 1
print(ans)

