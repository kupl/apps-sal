L,R = map(int,input().split())
MOD = 2019
ans = 2020
if R - L > 2010:
  print(0)
  return
for i in range(L,R):
    for j in range(i+1,R+1):
        ans = min(ans,i*j%MOD)
print(ans)
