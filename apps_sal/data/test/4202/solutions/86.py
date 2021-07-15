L,R = map(int,input().split())

if R-L > 2019:
  print(0)
  return
  
res = 100000
for i in range(L,R):
  ii = i%2019
  for j in range(i+1,R+1):
    j %= 2019
    res = min(res,ii*j%2019)
  
print(res)
