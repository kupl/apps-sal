X = int(input())
a = 0
if X == 2 or X == 3:
  print(X)
  return
if X % 2 == 0:
  X += 1
for i in range(X , 10 ** 6, 2):
  for j in range(3,i,2):
    a = i % j
    if a == 0:
      break
  if a != 0 :
    print(i)
    return
        
      
        

