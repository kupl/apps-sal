L, R = map(int, input().split())
 
m = 2019
flag = False
for i in range(L, R):
  for j in range(i+1, R+1):
    m = min(m, i*j % 2019)
    if m == 0: 
      flag = True
      break
  if flag: break
      
print(m)
