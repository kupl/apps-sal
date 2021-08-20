s = input()
x = s.count('o')
y = len(s) - x
if x <= 1:
    print('YES')
elif y % x == 0:
    print('YES')
else:
    print('NO')
