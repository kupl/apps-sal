s = input()
a1 = s.count('1')
a2 = s.count('2')
a3 = s.count('3')
if a3 == 0 and a2 == 0:
    print('1+' * (a1 - 1), '1', sep = '')
elif a3 == 0:
    print('1+' * a1, '2+' * (a2 - 1), '2', sep = '')
else:
    print('1+' * a1, '2+' * a2, '3+' * (a3 - 1), '3', sep = '')
