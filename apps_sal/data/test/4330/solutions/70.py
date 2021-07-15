a=sorted(list(map(int,input().split())))
if a[1]%2==a[0]%2:
  print(a[0]+(a[1]-a[0])//2)
else:
  print('IMPOSSIBLE')
