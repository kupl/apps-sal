l,r = map(int,input().split())
ans = 2019
for i in range(l,r+1):
  for j in range(i+1,r+1):
    ans = min(ans,(i*j)%2019)
    if ans == 0:
      print(0)
      return
print(ans)
