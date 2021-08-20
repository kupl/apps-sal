a = input().strip()
a = a + ''.join(list(reversed(input().strip())))
b = input().strip()
b = b + ''.join(list(reversed(input().strip())))
a = a.replace('X', '')
b = b.replace('X', '')
f = False
for i in range(4):
    if a == b:
        f = True
    b = b[1:] + b[:1]
if f:
    print('YES')
else:
    print('NO')
