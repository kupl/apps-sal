K =int(input())
a = 0
b = 1

for k in range(K):
  a+=b
  print(a)
  
  if b<(a+b)/sum(map(int,str(a+b))):
    b*=10
