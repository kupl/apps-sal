n = int(input())

a = n//7
b = n//4

for i in range(a+1):
  for j in range(b+1):
    if 7*i+4*j==n:
      print('Yes')
      return
    
print('No')
