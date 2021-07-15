N = int(input())
c = 0

for i in range(25):
  for j in range(14):
    if i*4 + j*7 == N:
      print("Yes")
      c += 1 
      return
    else:
      pass

if c == 0:
   print("No")
else:
  pass
