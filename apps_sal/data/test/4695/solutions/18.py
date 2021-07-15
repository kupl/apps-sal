x, y = list(map(int, input().split()))
a = [1, 3, 5, 7, 8, 10, 12]
b = [4, 6, 9, 11]
c = [2]

if x in a and x not in b and x not in c and y in a and y not in b and y not in c:
  print('Yes')
elif x not in a and x in b and x not in c and y not in a and y in b and y not in c :
  print('Yes')
else:
  print('No')

