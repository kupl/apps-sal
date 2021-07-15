N=str(input())
f=0
for i in range(len(N)):
  f=f+int(N[i])
if int(N)%f==0:
  print("Yes")
else:
  print("No")
