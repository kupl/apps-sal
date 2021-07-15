n = input()
res=0
for i in range(len(n)):
  res+= int(n[i])
  
n = int(n)
if n%res==0:
  print('Yes')
else:
  print('No')

