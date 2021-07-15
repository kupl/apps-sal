a,b,c = map(int,input().split())
q = a-b
ans = c-q

if ans < 0:
  ans = 0
  
print(ans)
