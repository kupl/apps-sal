x, y = map(int,input().split())
ans = 1
while x * 2 <= y:
  x *= 2
  ans += 1
print(ans)
