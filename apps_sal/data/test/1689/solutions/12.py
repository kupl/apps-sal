n = int(input())
bus = [input() for x in range(n)]
if 'OO' in ' '.join(bus):
    print('YES')
    found = False
    for line in bus:
        if 'OO' in line and (not found):
            found = True
            if line[:2] == 'OO':
                print('++' + line[2:])
            else:
                print(line[:3] + '++')
        else:
            print(line)
else:
    print('NO')
