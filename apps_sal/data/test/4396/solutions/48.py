n=int(input())
ans=0
for i in range(n):
  a,b=map(str, input().split())
  if b=='JPY':
    ans+=float(a)
  else:
    ans+=float(a)*380000
print(ans)
