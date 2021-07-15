n = input()
n = n[::-1]
for d in n:
    if d == '0':
        print('O-|-OOOO')
    if d == '1':
        print('O-|O-OOO')
    if d == '2':
        print('O-|OO-OO')
    if d == '3':
        print('O-|OOO-O')
    if d == '4':
        print('O-|OOOO-')
    if d == '5':
        print('-O|-OOOO')
    if d == '6':
        print('-O|O-OOO')
    if d == '7':
        print('-O|OO-OO')
    if d == '8':
        print('-O|OOO-O')
    if d == '9':
        print('-O|OOOO-')
