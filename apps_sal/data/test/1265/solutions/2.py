3

a = input()
b = input()
if len(a) != len(b) or (a.find('1') == -1) ^ (b.find('1') == -1):
    print('NO')
else:
    print('YES')

