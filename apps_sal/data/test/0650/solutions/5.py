a = 'AEFHIKLMNTVWXYZ'
b = 'BCDGJOPQRSU'
s = input()
ina = True
inb = True
for x in s:
    if x not in a:
        ina = False
    if x not in b:
        inb = False
if ina or inb:
    print('YES')
else:
    print('NO')
