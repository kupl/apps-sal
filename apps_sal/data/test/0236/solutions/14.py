c1 = c2 = 0
for i in input():
    if i == 'o':
        c2 += 1
    else:
        c1 += 1
if c2 == 0:
    print('YES')
elif c1 % c2:
    print('NO')
else:
    print('YES')
