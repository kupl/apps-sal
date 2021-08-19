zw = [True, False, False, False, True, True, False, True, True, False, True, True, True, True, False, False, False, False, False, True, False, True, True, True, True, True]
h = True
s = input()
b = zw[ord(s[0]) - 65]
for i in s:
    if b != zw[ord(i) - 65]:
        h = False
        break
if h:
    print('YES')
else:
    print('NO')
