N=int(input())
l=[]
for i in range(9):
  for j in range(9):
    l.append((i+1)*(j+1))
if N in l:
  print("Yes")
else:
    print("No")
