n = int(input())
res = []
fl = True
for i in range(n):
    line = input()
    if 'OO' in line and fl:
        fl = False
        line = line.split('|')
        if line[0] == 'OO':
            line[0] = '++'
        else:
            line[1] = '++'
        res.append(line[0]+'|'+line[1])
    else:
        res.append(line)
if not fl:
    print('YES')
    for i in res:
        print(i)
else:
    print('NO')
