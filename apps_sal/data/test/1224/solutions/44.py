N=int(input())
A = 1
for a in range(1,100):
  A *= 3
  B = 1
  for b in range(1,100):
    B *= 5
    if N == A + B:
      print(a,b)
      break
  else:
    continue
  break
else:
  print(-1)
