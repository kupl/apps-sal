a = input()
a = a + input()[::-1]
a = a.replace('X', '')
b = input()
b = b + input()[::-1]
b = b.replace('X', '')
b = b * 2

if b.find(a) == -1:
    print('NO')
else:
    print('YES')
