a = input()
b = input()

if len(a) != len(b):
    print('NO')
elif a == b:
    print('YES')
else:
    s = '0' * len(a)
    if a == s or b == s:
        print('NO')
    else:
        print('YES')
