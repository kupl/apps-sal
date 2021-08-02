X, Y = [x for x in input().split()]

if ord(X) < ord(Y):
    print('<')
elif ord(X) == ord(Y):
    print('=')
else:
    print('>')
