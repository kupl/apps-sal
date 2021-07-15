input()
x = y = 0
for t in map(int, input().split()):
  k = t - 25
  if y >= k // 50:
    y -= k // 50
    k -= 50 * (k // 50)
  if x >= k // 25:
    x -= k // 25
    k -= 25 * (k // 25)
  if k > 0:
    print("NO")
    return
  if t == 25:
    x += 1
  elif t == 50:
    y += 1    
print("YES")
