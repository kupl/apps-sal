X = int(input())


while True:
  a = []
  for i in range(2,X):
    if X % i == 0:
      a.append(0)
      break
    else:
      a.append(1)
  
  if 0 in a:
    X += 1
  else:
    break

print(X)
