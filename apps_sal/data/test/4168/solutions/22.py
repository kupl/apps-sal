N=int(input())

if N >= 0:
  n = N
  i = 0
  while 1:
    b = bin(n)[2:]
    if i >= len(b):
      break
    if i % 2 == 1 and b[-i-1]=='1':
      n += 2**(i+1)
    i += 1
  print(bin(n)[2:])
  
else:
  n = -N
  i = 0
  while 1:
    b = bin(n)[2:]
    if i >= len(b):
      break
    if i % 2 == 0 and b[-i-1]=='1':
      n += 2**(i+1)
    i += 1
  print(bin(n)[2:])
