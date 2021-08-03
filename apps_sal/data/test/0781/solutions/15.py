e = True
for i in range(8):
    a = input()
    if(a != 'BW' * 4) & (a != 'WB' * 4):
        e = False
        print('NO')
        break
if e:
    print('YES')
