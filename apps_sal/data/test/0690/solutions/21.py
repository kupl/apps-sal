def printDigit(d):
    if d == '0':
        print('O-|-OOOO')
    elif d == '1':
        print('O-|O-OOO')
    elif d == '2':
        print('O-|OO-OO')
    elif d == '3':
        print('O-|OOO-O')
    elif d == '4':
        print('O-|OOOO-')
    elif d == '5':
        print('-O|-OOOO')
    elif d == '6':
        print('-O|O-OOO')
    elif d == '7':
        print('-O|OO-OO')
    elif d == '8':
        print('-O|OOO-O')
    elif d == '9':
        print('-O|OOOO-')


n = int(input())
n = str(n)
n = list(n)
n.reverse()
for d in n:
    printDigit(d)
