a = input()
b = input()
c = input()

turn = 'a'
while True:
    if turn == 'a':
        if a == '':
            print('A')
            return
        elif a[0] == 'a':
            turn = 'a'
        elif a[0] == 'b':
            turn = 'b'
        else:
            turn = 'c'
        a = a[1:]
    elif turn == 'b':
        if b == '':
            print('B')
            return
        elif b[0] == 'a':
            turn = 'a'
        elif b[0] == 'b':
            turn = 'b'
        else:
            turn = 'c'
        b = b[1:]
    else:
        if c == '':
            print('C')
            return
        elif c[0] == 'a':
            turn = 'a'
        elif c[0] == 'b':
            turn = 'b'
        else:
            turn = 'c'
        c = c[1:]

