N = int(input())

if N == 1:
  print(1)
  return

L1 = 1
L0 = 2

for i in range(2,N+1):
  LC = L1 + L0
  L0 = L1
  L1 = LC
  
print(LC)
