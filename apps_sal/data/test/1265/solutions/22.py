a = input()
b = input()
if len(a) != len(b):
    print('NO')
elif a == b:
    print('YES')
elif '1' in a and '1' in b:
    print('YES')
else:
    print('NO')
