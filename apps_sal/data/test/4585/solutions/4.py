x=int(input())
a=0
for i in range(x+1):
  if a+i>=x:
    print(i)
    break
  else:
    a+=i
