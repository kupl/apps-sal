n = int(input())
a = input()
o = a.count('1')
if o == n or o == 0:
  print(a)
else:
  print('2 1 ' + '2 ' * (n - o - 1) + '1 ' * (o - 1))

