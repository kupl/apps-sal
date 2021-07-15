n = int(input().strip())
tmp =[]
i=2
while(i<=n):
  tmp.append(i)
  i = i+2
i =1
while(i<=n):
  tmp.append(i)
  i = i+2
i=2
while(i<=n):
  tmp.append(i)
  i = i+2
print(len(tmp))
print(' '.join(map(str,tmp)))
