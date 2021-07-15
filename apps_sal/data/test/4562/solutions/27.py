n=int(input())
i=1
tmp=1
while True:
  if i**2 <= n:
    tmp = i**2
  else:
    break
  i += 1
print(tmp)
