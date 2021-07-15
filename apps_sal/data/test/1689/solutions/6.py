n = int(input())
seat = []
for nn in range(n):
    seat.append(input())

ok = False

for i in range(n):
    a,b = seat[i].split('|')
    if ok is False:
        if a == 'OO':
            a = '++'
            ok = True
        elif b == 'OO':
            b = '++'
            ok = True
    seat[i] = a + '|' + b

if ok is False:
    print('NO')
    return
else:
    print('YES')
    print('\n'.join(seat))
