a = input()
b = input()
n = len(a)
if n != len(b):
    print('NO')
    return
if n == 1 and a != b:
    print('NO')
    return
if (a.count('1') > 0) == (b.count('1') > 0):
    print('YES')
else:
    print('NO')
