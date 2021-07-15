A,B = input().split()
A = int(A)
B = B[0]+B[2:]

if A*int(B) >= 100:
  print(str(A*int(B))[:-2])
else:
  print(0)
