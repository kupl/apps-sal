lst = input().split()
a = int(lst[0])
b = int(lst[1])
x = int(lst[2])

if (x <= a + b) and (a <= x):
   print('YES')
else:
   print('NO')
