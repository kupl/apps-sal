t=int(input())
for _ in range(t):
  x,n,m=map(int,input().split())
  for _ in range(n):
    if x<=20:
      break
    x=x//2+10
  if 10*m>=x:
    print('YES')
  else:
    print('NO')
