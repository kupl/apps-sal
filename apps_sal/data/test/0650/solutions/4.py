n = input()
s = 'AEFHIKLMNTVWXYZ'
t = 'BCDGJOPQRSU'
f1 = 0
f2 = 0
for i in s:
    if i in n:
        f1 = 1
for i in t:
    if i in n:
        f2 = 1
if f1 + f2 == 1:
    print('YES')
else:
    print('NO')
