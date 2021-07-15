a = int(input())
if a == 1:
  print('Hello World')
else:
  a = [int(input()) for i in range(2)]
  print(a[0] + a[1])
