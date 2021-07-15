n = int(input())
lst = []
d = dict()
for temp in range(n):
  input_str, z = input().split('/')
  x, y = input_str.split('+')
  x = x [1:]
  y = y [:len(y)-1]
  x = int(x)
  y = int(y)
  z = int(z)
  ans = (x+y)/z
  if(ans in d.keys()) : d[ans]+=1
  else : d[ans]=1
  lst.append(ans)
for i in lst:
  print(d[i], end=" ")
