a, b  = map(int,input().split())
c = b - a
ans = 0
for i in range(c):
  ans += i
  
print(ans - a)
