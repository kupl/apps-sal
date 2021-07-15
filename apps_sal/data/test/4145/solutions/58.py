n=int(input())
while True:
  j=True
  for i in range(2,int(n**.5)+1):
    if n%i==0:
      n+=1
      j=False
      break
  if j:
    print(n)
    break
