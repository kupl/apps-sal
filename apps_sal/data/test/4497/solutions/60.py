N=int(input())
result=64
while N>=1:
  if N >= result:
    print(result)
    break
  result=int(result/2)
else:
  print(result)
