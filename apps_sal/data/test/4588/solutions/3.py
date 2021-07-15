X, Y = map(ord, input().split())
if X < Y:
    print('<')
elif X > Y:
    print('>')
else:
    print('=')
