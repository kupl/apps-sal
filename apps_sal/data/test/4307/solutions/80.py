n = int(input())
 
def check(p):
  c = 0
  for i in range(1,p+1):
    if p % i == 0:
      c += 1
  return c
 
ans = 0
for i in range(1,n+1):
  if i % 2 == 1:
    if check(i) == 8:
      ans += 1
      
print(ans)
