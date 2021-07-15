s = input()
x = s.count('o')
y = s.count('-')
if x == 0 or y == 0:
    print('YES')
else:
    print('YES' if y % x == 0 else 'NO')
