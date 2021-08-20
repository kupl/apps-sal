s = input()
t = s.count('o')
c = s.count('-')
if t == 0 or c % t == 0:
    print('YES')
else:
    print('NO')
