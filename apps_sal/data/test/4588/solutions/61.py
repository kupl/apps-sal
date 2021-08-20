(X, Y) = [int('0x' + i, base=16) for i in input().split()]
if X > Y:
    print('>')
elif X < Y:
    print('<')
else:
    print('=')
