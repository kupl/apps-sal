N = int(input())
S = []

for i in range(1, 10):
  for j in range(1, 10):
    S.append(i*j)
    
if N in S:
  print("Yes")

else:
  print("No")
