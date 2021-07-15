x, y, z = map(int, input().split())

ans = 0
ans2 = 0
ans += x // z 
ans += y // z 
x %= z 
y %= z

if x + y >= z:
  ans += 1
  ans2 = min(z - x, z - y)

print(ans, ans2) 
