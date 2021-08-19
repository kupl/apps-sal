s = input()
b = s.count('o')
n = s.count('-')
if n == 0 or b == 0:
    print('YES')
elif n % b == 0:
    print('YES')
else:
    print('NO')
