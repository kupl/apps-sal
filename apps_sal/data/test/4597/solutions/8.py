a=int(input())
b=1
for i in range(1,a+1):
  b=b*i
  if b>1000000007:
    b=b%1000000007
if b<1000000000:
  print(b)
else:
  print((b%1000000007))

