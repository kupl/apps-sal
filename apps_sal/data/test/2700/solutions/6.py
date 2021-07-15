t = eval(input())
while t:
 a,b,c,d = list(map(int, input().split()))
 ans = 0
 if c<= d:
  for x in range(a,b+1):
   y = x+1
   if c > y: y = c
   if d-y >= 0: ans += d-y+1
 print(ans)
 t -= 1
