x = []
x.append((len(input()) - 2, 'A'))
x.append((len(input()) - 2, 'B'))
x.append((len(input()) - 2, 'C'))
x.append((len(input()) - 2, 'D'))

x.sort()

if x[0][0] * 2 <= x[1][0] and x[2][0] * 2 <= x[3][0]:
    print('C')
else:
    if x[0][0] * 2 <= x[1][0]:
        print(x[0][1])
    else:
        if x[2][0] * 2 <= x[3][0]:
            print(x[3][1])
        else:
            print('C')
