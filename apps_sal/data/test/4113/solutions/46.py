n=int(input())
if n>=28:
  print('Yes')
else:
  ans='No'
  for i in range(8):
    for j in range(5):
      if i*4+j*7==n:
        ans='Yes'
  print(ans)
