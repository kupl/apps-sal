s = input()
a = 0
b = 0
c = 0
if ''.join(sorted(s)) == s:
    for i in s:
        if i == 'a':
            a += 1
        elif i == 'b':
            b += 1
        elif i == 'c':
            c += 1
    if a > 0 and b > 0 and (c == a or c == b):
        print('YES')
    else:
        print('NO')
else:
    print('NO')
