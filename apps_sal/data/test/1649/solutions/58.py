a=list(map(int,input().split()))
for i in range(16):
 r=0
 for j,k in enumerate(map(int,bin(i)[2:].zfill(4))):
  r+=a[j]*k
 if r==sum(a)/2:
  print("Yes")
  return
print("No")
