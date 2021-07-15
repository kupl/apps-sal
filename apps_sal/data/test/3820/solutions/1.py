input()
a = input()
b = input()

if '*' in a:
    x, y = a.split('*')
    if b.startswith(x) and b.endswith(y) and len(b) >= (len(x) + len(y)):
        print('YES')
    else:
        print('NO')
else:
    print('YES' if a == b else 'NO')

