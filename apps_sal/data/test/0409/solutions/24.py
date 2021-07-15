s = input()
i = s.find('AB')
j = s.find('BA')
if i != -1 and s.find('BA', i + 2) != -1:
    print('YES')
elif j != -1 and s.find('AB', j + 2) != -1:
    print('YES')
else:
   print('NO')

