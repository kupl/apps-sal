x = int(input())
ans = 1
for b in range(2,int(x**0.5)+1):
  for p in range(2,10):
    c = b**p
    if c > x:
      break
    ans = max(ans,c)
print(ans)
