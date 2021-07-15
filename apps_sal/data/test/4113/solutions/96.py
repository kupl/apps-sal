N=int(input())
for i in range(0,4):
  if N-7*i>=0 and (N-7*i)%4==0:
    print("Yes")
    break
else:
  print("No")
