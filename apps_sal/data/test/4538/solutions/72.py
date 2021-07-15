n,d = map(int,input().split())
ans = 0

for i in range(n):
  x,y = map(int,input().split())
  if d >= (x**2 + y**2)**0.5:
    ans += 1
    
print(ans)
