p,x,y = list(map(int,input().split()))
ls = []
i = x//50 % 475
for z in range(25):
  i = (i*96 + 42) % 475
  ls.append(i+26)
if p in ls:
  print(0)
  quit()
l = x-50
m = x
while l >= y:
  ls = []
  i = l//50 % 475
  for z in range(25):
    i = (i*96 + 42) % 475
    ls.append(i+26)
  if p in ls:
    print(0)
    quit()
  l-=50
index = 1
while True:
  ls = []
  i = (m+index*50)//50 % 475
  for z in range(25):
    i = (i*96 + 42) % 475
    ls.append(i+26)
  if p in ls:
    print((50*index + 50)//100)
    break
  else:
    index += 1
  

