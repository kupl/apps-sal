s = input()
c = 0
for i in s:
    if i == 'a':
        c = c + 1
nb = len(s) - c
if nb % 2 == 0:
    nb = nb // 2
    a = s[:nb + c]
    b = s[nb + c:]
    z = ''
    for i in a:
        if i != 'a':
            z = z + i
    if z == b:
        print(a)
    else:
        print(':(')
else:
    print(':(')
